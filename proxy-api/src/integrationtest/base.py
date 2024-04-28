import unittest
import requests

class IntegrationTest(unittest.TestCase):
    def setUp(self):
        self.TARGET_URL = "http://localhost:7071/api"

    def set_target_url(self, url):
        self.TARGET_URL = url

    def test_health_check(self):
        url = f'{self.TARGET_URL}/health-check'
        response = requests.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "ok")

    def test_digital_go_geocode(self):
        url = f'{self.TARGET_URL}/digital-go-geocode?address=北九州市若松区響町一丁目'
        response = requests.get(url).json()

        self.assertEqual(response['lg_code'], '401030')
        self.assertEqual(response['town_id'], '0075001')
        self.assertEqual(response['fulladdress'], '福岡県北九州市若松区響町一丁目')
        self.assertEqual(response['prefecture'], '福岡県')
        self.assertEqual(response['city'], '北九州市若松区')
        self.assertEqual(response['town'], '響町一丁目')
        self.assertEqual(response['lat'], 33.940111)
        self.assertEqual(response['lon'], 130.821747)

    def test_japanese_to_english(self):
        url = f'{self.TARGET_URL}/japanese-to-english?jp=東京'
        response = requests.get(url).json()

        self.assertEqual(response["en"], "Tokyo")
    
if __name__ == '__main__':
    unittest.main()
