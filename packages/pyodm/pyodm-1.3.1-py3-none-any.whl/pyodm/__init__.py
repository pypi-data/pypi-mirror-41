"""
PyODM is a library for easily creating orthophotos, DEMs, 3D models and point clouds from images aerial images via the `NodeODM API`_. It is an official `OpenDroneMap`_ project.

Installation:
-------------

``pip install -U pyodm``

Simple usage:
-------------

To run these examples, start a new NodeODM node via:

``docker run -ti -p 3000:3000 opendronemap/nodeodm``

Then:

   >>> import os
   >>> from pyodm import Node
   >>> n = Node('localhost', 3000)
   >>> task = n.create_task(['examples/images/image_1.jpg', 'examples/images/image_2.jpg'], {'dsm': True})
   >>> task.wait_for_completion()
   >>> os.listdir(task.download_assets("results"))
   ['odm_orthophoto', 'odm_dem', 'images.json', 'odm_georeferencing', 'odm_texturing', 'dsm_tiles', 'dtm_tiles', 'orthophoto_tiles', 'potree_pointcloud']

Code Samples:
-------------
 * `Create Task`_
 * `Get Node Info`_

Getting Help / Reporting Issues:
--------------------------------

PyODM is in active development. If you find an issue please `report it`_. We welcome contributions, see the `GitHub`_ page for more information.

For all development questions, please reach out on the `Community Forum`_.

License: BSD 3-Clause, see LICENSE for more details.

.. _NodeODM API:
   https://github.com/OpenDroneMap/NodeODM/blob/master/docs/index.adoc
.. _OpenDroneMap:
    https://www.opendronemap.org
.. _Create Task:
   https://github.com/OpenDroneMap/PyODM/blob/master/examples/create_task.py
.. _Get Node Info:
   https://github.com/OpenDroneMap/PyODM/blob/master/examples/get_node_info.py
.. _report it:
    https://github.com/OpenDroneMap/PyODM/issues
.. _`GitHub`:
    https://github.com/OpenDroneMap/PyODM
.. _`Community Forum`:
    https://community.opendronemap.org
"""

name = "pyodm"
from .api import Node, Task