import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.utils import get_config
import unittest
import requests

class IntegrationTest(unittest.TestCase):
    TARGET_URL: str

    @classmethod
    def setUpClass(cls):
        config = get_config('prod.yaml')
        cls.TARGET_URL = config['deploy']['url']

    def test_hello(self):
        endpoint = '/hello'
        url = IntegrationTest.TARGET_URL + endpoint
        response = requests.get(url)

        self.assertEqual(response.text, "Hello World from /hello")

    def test_geocode(self):
        endpoint = '/geocode'
        params = '?city_block_id=3&residence_id=28&address=赤岩町'
        url = IntegrationTest.TARGET_URL + endpoint + params
        response = requests.get(url).json()

        self.assertEqual(response['code'], 401030)
        self.assertEqual(response['aza_id'], 4000)
        self.assertEqual(response['prefectures'], '福岡県')
        self.assertEqual(response['municipalities'], '北九州市若松区')
        self.assertEqual(response['aza'], '赤岩町')
        self.assertEqual(response['latitude'], 33.890251893)
        self.assertEqual(response['longitude'], 130.767441408)

    def test_digital_go_geocode(self):
        endpoint = '/digital-go-geocode'
        params = '?address=北九州市若松区響町一丁目'
        url = IntegrationTest.TARGET_URL + endpoint + params
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
        endpoint = '/japanese-to-english'
        params = '?jp=東京都'
        url = IntegrationTest.TARGET_URL + endpoint + params
        response = requests.get(url).json()

        self.assertEqual(response["en"], "Tokyo")

    def test_id(self):
        # IDのカウントリセット
        endpoint = '/id-reset'
        url = IntegrationTest.TARGET_URL + endpoint
        response = requests.get(url)

        endpoint = '/id'
        url = IntegrationTest.TARGET_URL + endpoint

        response = requests.get(url).json()
        self.assertEqual(response["id"], "0")

        response = requests.get(url).json()
        self.assertEqual(response["id"], "1")

    def test_id_header(self):
        # IDのカウントリセット
        endpoint = '/id-reset'
        url = IntegrationTest.TARGET_URL + endpoint
        response = requests.get(url)

        endpoint = '/id'
        params = '?header=test_'
        url = IntegrationTest.TARGET_URL + endpoint + params

        response = requests.get(url).json()
        self.assertEqual(response["id"], "test_0")

    def test_id_reset(self):
        endpoint = '/id-reset'

        url = IntegrationTest.TARGET_URL + endpoint
        response = requests.get(url)

        self.assertEqual(response.text, "Success")

    def test_poi(self):
        endpoint = '/poi'
        params = '?word=火山'
        url = IntegrationTest.TARGET_URL + endpoint + params
        response = requests.get(url).json()

        self.assertEqual(response["code"], 102)
    
if __name__ == '__main__':
    unittest.main()
