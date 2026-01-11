import unittest
from app import app
import time

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello World', response.data)
        self.assertIn(b'Application uptime:', response.data)

    def test_uptime_increases(self):
        initial_response = self.app.get('/')
        time.sleep(1)
        second_response = self.app.get('/')
        self.assertNotEqual(initial_response.data, second_response.data)

if __name__ == '__main__':
    unittest.main()
