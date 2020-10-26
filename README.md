# Python package for IoTDB

This module contains the missing parts from the `apache-iotdb` package which can be found here https://pypi.org/project/apache-iotdb/.

## Example

Just install the package via `pip install iotdb-session-0.10.1`.
The sessions API can be used via:

```
from iotdb_session.Session import Session

ip = "127.0.0.1"
port_ = "6667"
username_ = 'root'
password_ = 'root'
session = Session(ip, port_, username_, password_)
session.open(False)
zone = session.get_time_zone()
session.close()

self.assertEqual("+08:00", zone)
```