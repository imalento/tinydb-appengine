# tinydb-appengine

__tinydb-appengine__ provides TinyDB storage for App Engine. You can use JSON readonly.

## Installation

```bash
$ pip install tinydb-appengine
```

## Usage

```python
from tinydb import TinyDB
from tinydb_appengine.storages import EphemeralJSONStorage
db = TinyDB('your_data.json', storage=EphemeralJSONStorage)
```
