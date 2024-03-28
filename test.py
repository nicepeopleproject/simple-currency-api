import unittest
import requests

class TestCurrencyRate(unittest.TestCase):
    def test_get_currency_rate_handler(self):
        url = 'http://127.0.0.1:5000/get_currency_rate'
        currency = 'USD'
        data = {'currency': currency}
        response = requests.post(url, json=data)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('currency', data)
        self.assertEqual(data['currency'], currency)
        self.assertIn('rate', data)
        self.assertIsInstance(data['rate'], float)

if __name__ == '__main__':
    unittest.main()