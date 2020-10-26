import unittest

from iotdb_session.Session import Session


class TestIntegration(unittest.TestCase):

    def test_connect(self):
        ip = "127.0.0.1"
        port_ = "6667"
        username_ = 'root'
        password_ = 'root'
        session = Session(ip, port_, username_, password_)
        session.open(False)
        zone = session.get_time_zone()
        session.close()

        self.assertEqual("+08:00", zone)


if __name__ == '__main__':
    unittest.main()
