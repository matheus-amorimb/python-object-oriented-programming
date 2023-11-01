import unittest
from datetime import timedelta
from src.TimeZone import TimeZone

class TestTimeZone(unittest.TestCase):

    def test_create_timezone(self):
        tz = TimeZone('ABC', -1)
        self.assertEqual('ABC', tz.name)
        self.assertEqual(timedelta(hours=-1), tz.offset)