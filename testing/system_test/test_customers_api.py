import unittest
import requests


class TestCustomersApi(unittest.TestCase):

    def setUp(self):
        self.url = "http://localhost:5000"

    def test_maintenance(self):
        response = requests.get(self.url + "/customers")
        self.assertEqual(200, response.status_code)

        response = requests.post(self.url + "/customers", json={
            "name": "customer_test"
        })
        self.assertEqual(200, response.status_code)

