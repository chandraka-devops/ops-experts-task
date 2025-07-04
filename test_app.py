import unittest
from app import app


class ChandraGistTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_get_valid_user(self):
        response = self.client.get('/octocat')
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertIsInstance(data, list)

        if data:
            self.assertIn('id', data[0])
            self.assertIn('url', data[0])

    def test_get_invalid_user(self):
        response = self.client.get('/nonexistentuser123456789')
        self.assertIn(response.status_code, [404, 403])
        self.assertIn('error', response.get_json())


if __name__ == '__main__':
    unittest.main()
