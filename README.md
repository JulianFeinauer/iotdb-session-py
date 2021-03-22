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

## Test Support for IoTDB

The Test Support is based on the lib `testcontainers` (https://testcontainers-python.readthedocs.io/en/latest/index.html) which you need to install in your project if you want to use the feature.

To start (and stop) an IoTDB Database in a Docker container simply do:
```
class MyTestCase(unittest.TestCase):

    def test_something(self):
        with IoTDBContainer() as c:
            session = Session('localhost', c.get_exposed_port(6667), 'root', 'root')
            session.open(False)
            result = session.execute_query_statement("SHOW TIMESERIES")
            print(result)
            session.close()
```

## Release Notes

**0.1.5** - Fixed a bug that avoided Type Inference on the server
* insert_record can now be called without dataTypes argument
* then the server will perform type inference

**0.1.4** - Improved Testcontainer: 
* Use real containerip
* Use Tag 0.10.1 not latest