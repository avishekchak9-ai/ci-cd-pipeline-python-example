# test_app.py
import unittest
from app import app
class BasicTests(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
    def test_main_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello from Python CI/CD Pipeline', response.data)
    def test_main_page_version(self):
        response = self.app.get('/')
        self.assertIn(b'v1.0', response.data)
if __name__ == '__main__':
    unittest.main()
