"""
API
======
"""
import zipfile

import requests
import mimetypes
import json
import os
from urllib.parse import urlunparse, urlencode, urlparse, parse_qs

try:
    import simplejson as json
except ImportError:
    import json
import time

from urllib3.exceptions import ReadTimeoutError

from pyodm.types import NodeOption, NodeInfo, TaskInfo, TaskStatus
from .exceptions import NodeConnectionError, NodeResponseError, NodeServerError, TaskFailedError
from .utils import MultipartEncoder, options_to_json
from requests_toolbelt.multipart import encoder


class Node:
    """A client to interact with NodeODM API.

        Args:
            host (str): Hostname or IP address of processing node
            port (int): Port of processing node
            token (str): token to use for authentication
            timeout (int): timeout value in seconds for network requests
    """

    def __init__(self, host, port, token="", timeout=30):
        self.host = host
        self.port = port
        self.token = token
        self.timeout = timeout

    @staticmethod
    def from_url(url, timeout=30):
        """Create a Node instance from a URL.

        >>> n = Node.from_url("http://localhost:3000?token=abc")

        Args:
            url (str): URL in the format proto://hostname:port/?token=value
            timeout (int): timeout value in seconds for network requests

        Returns:
            :func:`~Node`
        """
        u = urlparse(url)
        qs = parse_qs(u.query)

        port = u.port
        if port is None:
            port = 443 if u.scheme == 'https' else 80

        token = ""
        if 'token' in qs:
            token = qs['token'][0]

        return Node(u.hostname, port, token, timeout)

    def url(self, url, query={}):
        """Get a URL relative to this node.

        Args:
            url (str): relative URL
            query (dict): query values to append to the URL

        Returns:
            str: Absolute URL
        """
        netloc = self.host if (self.port == 80 or self.port == 443) else "{}:{}".format(self.host, self.port)
        proto = 'https' if self.port == 443 else 'http'

        if len(self.token) > 0:
            query['token'] = self.token

        return urlunparse((proto, netloc, url, '', urlencode(query), ''))

    def get(self, url, query={}, **kwargs):
        try:
            res = requests.get(self.url(url, query), timeout=self.timeout, **kwargs)
            if res.status_code == 401:
                raise NodeResponseError("Unauthorized. Do you need to set a token?")
            elif res.status_code != 200 and res.status_code != 403:
                raise NodeServerError(res.status_code)

            if "Content-Type" in res.headers and "application/json" in res.headers['Content-Type']:
                return res.json()
            else:
                return res
        except json.decoder.JSONDecodeError as e:
            raise NodeServerError(str(e))
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
            raise NodeConnectionError(str(e))

    def post(self, url, data, headers={}):
        try:
            res = requests.post(self.url(url), data=data, headers=headers, timeout=self.timeout)

            if res.status_code == 401:
                raise NodeResponseError("Unauthorized. Do you need to set a token?")
            elif res.status_code != 200 and res.status_code != 403:
                raise NodeServerError(res.status_code)

            if "Content-Type" in res.headers and "application/json" in res.headers['Content-Type']:
                return res.json()
            else:
                return res
        except json.decoder.JSONDecodeError as e:
            raise NodeServerError(str(e))
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
            raise NodeConnectionError(str(e))


    def info(self):
        """Retrieve information about this node.

        >>> n = Node('localhost', 3000)
        >>> n.info().version
        '1.3.1'

        Returns:
            :func:`~pyodm.types.NodeInfo`
        """
        return NodeInfo(self.get('/info'))

    def options(self):
        """Retrieve the options available for creating new tasks on this node.

        >>> n = Node('localhost', 3000)
        >>> n.options()[0].name
        'pc-classify'
        >>> n.options()[0].domain
        ['none', 'smrf', 'pmf']

        Returns:
            list: [:func:`~pyodm.types.NodeOption`]
        """
        return list(map(lambda o: NodeOption(**o), self.get('/options')))

    def create_task(self, files, options={}, name=None, progress_callback=None):
        """Start processing a new task.
        At a minimum you need to pass a list of image paths. All other parameters are optional.

        >>> n = Node('localhost', 3000)
        >>> t = n.create_task(['examples/images/image_1.jpg', 'examples/images/image_2.jpg'], \
                          {'orthophoto-resolution': 2, 'dsm': True})
        >>> info = t.info()
        >>> info.status
        <TaskStatus.RUNNING: 20>
        >>> t.info().images_count
        2
        >>> t.output()[0:2]
        ['DJI_0131.JPG - DJI_0313.JPG has 1 candidate matches', 'DJI_0131.JPG - DJI_0177.JPG has 3 candidate matches']


        Args:
            files (list): list of image paths + optional GCP file path.
            options (dict): options to use, for example {'orthophoto-resolution': 3, ...}
            name (str): name for the task
            progress_callback (function): callback reporting upload progress percentage

        Returns:
            :func:`~Task`
        """
        if len(files) == 0:
            raise NodeResponseError("Not enough images")

        # Equivalent as passing the open file descriptor, since requests
        # eventually calls read(), but this way we make sure to close
        # the file prior to reading the next, so we don't run into open file OS limits
        def read_file(file_path):
            with open(file_path, 'rb') as f:
                return f.read()

        fields = {
            'name': name,
            'options': options_to_json(options),
            'images': [(os.path.basename(f), read_file(f), (mimetypes.guess_type(f)[0] or "image/jpg")) for
                       f in files]
        }

        def create_callback(mpe):
            total_bytes = mpe.len

            def callback(monitor):
                if progress_callback is not None and total_bytes > 0:
                    progress_callback(100.0 * monitor.bytes_read / total_bytes)

            return callback

        e = MultipartEncoder(fields=fields)
        m = encoder.MultipartEncoderMonitor(e, create_callback(e))

        try:
            result = self.post('/task/new', data=m, headers={'Content-Type': m.content_type})
        except (json.decoder.JSONDecodeError, simplejson.JSONDecodeError) as e:
            raise NodeServerError(str(e))
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
            raise NodeConnectionError(e)

        if 'uuid' in result:
            return Task(self, result['uuid'])
        elif 'error' in result:
            raise NodeResponseError(result['error'])
        else:
            raise NodeServerError('Invalid response: ' + str(result))

    def get_task(self, uuid):
        """Helper method to initialize a task from an existing UUID

        >>> n = Node("localhost", 3000)
        >>> t = n.get_task('00000000-0000-0000-0000-000000000000')
        >>> t.__class__
        <class 'pyodm.api.Task'>

        Args:
            uuid: Unique identifier of the task
        """
        return Task(self, uuid)

class Task:
    """A task is created to process images. To create a task, use :func:`~Node.create_task`.

    Args:
        node (:func:`~Node`): node this task belongs to
        uuid (str): Unique identifier assigned to this task.
    """

    def __init__(self, node, uuid):
        self.node = node
        self.uuid = uuid


    def get(self, url, query = {}, **kwargs):
        result = self.node.get(url, query, **kwargs)
        if isinstance(result, dict) and 'error' in result:
            raise NodeResponseError(result['error'])
        return result

    def post(self, url, data):
        result = self.node.post(url, data)
        if isinstance(result, dict) and 'error' in result:
            raise NodeResponseError(result['error'])
        return result

    def info(self):
        """Retrieves information about this task.

        Returns:
            :func:`~pyodm.types.TaskInfo`
        """
        return TaskInfo(self.get('/task/{}/info'.format(self.uuid)))

    def output(self, line=0):
        """Retrieve console task output.

        Args:
            line (int): Optional line number that the console output should be truncated from.
            For example, passing a value of 100 will retrieve the console output starting from
            line 100. Negative numbers are also allowed. For example -50 will retrieve the last
            50 lines of console output. Defaults to 0 (retrieve all console output).

        Returns:
            [str]: console output (one list item per row).
        """
        return self.get('/task/{}/output'.format(self.uuid), {'line': line})

    def cancel(self):
        """Cancel this task.

        Returns:
            bool: task was canceled or not
        """
        return getattr(self.post('/task/cancel', {'uuid': self.uuid}), 'success', False)

    def remove(self):
        """Remove this task.

        Returns:
            bool: task was removed or not
        """
        return getattr(self.post('/task/remove', {'uuid': self.uuid}), 'success', False)

    def restart(self, options=None):
        """Restart this task.

        Args:
            options (dict): options to use, for example {'orthophoto-resolution': 3, ...}

        Returns:
            bool: task was restarted or not
        """
        data = {'uuid': self.uuid}
        if options is not None: data['options'] = options_to_json(options)
        return getattr(self.post('/task/restart', data), 'success', False)

    def download_zip(self, destination, progress_callback=None):
        """Download this task's assets archive to a directory.

        Args:
            destination (str): directory where to download assets archive. If the directory does not exist, it will be created.
            progress_callback (function): an optional callback with one parameter, the download progress percentage
        Returns:
            str: path to archive file (.zip)
        """
        info = self.info()
        if info.status != TaskStatus.COMPLETED:
            raise NodeResponseError("Cannot download task, task status is " + str(info.status))

        if not os.path.exists(destination):
            os.makedirs(destination, exist_ok=True)

        try:
            download_stream = self.get('/task/{}/download/all.zip'.format(self.uuid), stream=True)
            zip_path = os.path.join(destination, "{}_{}_all.zip".format(self.uuid, int(time.time())))

            # Keep track of download progress (if possible)
            content_length = download_stream.headers.get('content-length')
            total_length = int(content_length) if content_length is not None else None
            downloaded = 0

            with open(zip_path, 'wb') as fd:

                for chunk in download_stream.iter_content(4096):
                    downloaded += len(chunk)

                    if progress_callback is not None:
                        progress_callback((100.0 * float(downloaded) / total_length))

                    fd.write(chunk)
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError, ReadTimeoutError) as e:
            raise NodeConnectionError(e)

        return zip_path

    def download_assets(self, destination, progress_callback=None):
        """Download this task's assets to a directory.

        Args:
            destination (str): directory where to download assets. If the directory does not exist, it will be created.
            progress_callback (function): an optional callback with one parameter, the download progress percentage
        Returns:
            str: path to saved assets
        """
        zip_path = self.download_zip(destination, progress_callback=progress_callback)
        with zipfile.ZipFile(zip_path, "r") as zip_h:
            zip_h.extractall(destination)
            os.remove(zip_path)

        return destination

    def wait_for_completion(self, status_callback=None, interval=3):
        """Wait for the task to complete. The call will block until the task status has become
        :func:`~TaskStatus.COMPLETED`. If the status is set to :func:`~TaskStatus.CANCELED` or :func:`~TaskStatus.FAILED`
        it raises a TaskFailedError exception.

        Args:
            status_callback (function): optional callback that will be called with task info updates every interval seconds.
            interval (int): seconds between status checks.
        """
        while True:
            info = self.info()

            if status_callback is not None:
                status_callback(info)

            if info.status in [TaskStatus.COMPLETED, TaskStatus.CANCELED, TaskStatus.FAILED]:
                break

            time.sleep(interval)

        if info.status in [TaskStatus.FAILED, TaskStatus.CANCELED]:
            raise TaskFailedError(info.status)
