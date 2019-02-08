tinydb-appengine
^^^^^^^^^^^^^^^^

``tinydb-appengine`` provides TinyDB storage for App Engine. You can use JSON readonly.

Installation
************

.. code-block:: bash

    $ pip install tinydb_appengine

Usage
*****

.. code-block:: python

    >>> from tinydb import TinyDB
    >>> from tinydb_appengine.storages import EphemeralJSONStorage
    >>> db = TinyDB('your_data.json', storage=EphemeralJSONStorage)

