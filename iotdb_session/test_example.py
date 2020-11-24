import unittest

from iotdb_session.Session import Session
from iotdb_session.container import IoTDBContainer


class MyTestCase(unittest.TestCase):

    def test_something(self):
        with IoTDBContainer() as c:
            session = Session('localhost', c.get_exposed_port(6667), 'root', 'root')
            session.open(False)
            result = session.execute_query_statement("SHOW TIMESERIES")
            print(result)
            session.close()
