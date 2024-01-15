import sys
import os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
# from src.service.digitalGeocodeService import DigitalGeocodeService
from src.domain.digitalGeocodeDomain import DigitalGeocodeDomain
from function_app import app

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_hello_endpoint(self):
        response = self.app.get('/hello')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Hello World from /hello', response.get_data(as_text=True))

    @patch('src.service.digitalGeocodeService.DigitalGeocodeService')
    def test_geocode_endpoint_with_address(self, mock_service):
        # モックオブジェクトを設定
        mock_service.return_value.get.return_value = DigitalGeocodeDomain(
            **{
                "output": "東京都千代田区紀尾井町1-3 東京ガーデンテラス紀尾井町 19階、20階",
                "prefecture": "東京都",
                "match_level": 8,
                "city": "千代田区",
                "town": "紀尾井町",
                "town_id": "0056000",
                "lg_code": "131016",
                "other": "ビル",
                "lat": 35.679107172,
                "lon": 139.736394597,
                "block": "1",
                "block_id": "001",
                "addr1": "3",
                "addr1_id": "003",
                "addr2": "3",
                "addr2_id": "003"
            }
        )

        # テスト対象のエンドポイントにリクエストを送信
        response = self.app.get('/digital_geocode', query_string={'address': '東京都千代田区紀尾井町1-3'})

        # ステータスコードとレスポンスの内容を検証
        self.assertEqual(response.status_code, 200)
        # ここでレスポンスの内容を確認するアサーションを追加

        # モックが期待通りに呼び出されたことを検証
        mock_service.return_value.get.assert_called_with('東京都千代田区紀尾井町1-3')


    # @patch('function_app.DigitalGeocodeService')
    # @patch('src.service.digitalGeocodeService.DigitalGeocodeService')
    # def test_geocode_endpoint_with_address(self, mock_service_class):
    #     # モックのインスタンスを作成し、その get メソッドの戻り値を設定
    #     mock_service_instance = MagicMock()
    #     mock_service_instance.get.return_value = DigitalGeocodeDomain(
    #         **{
    #             "output": "東京都千代田区紀尾井町1-3 東京ガーデンテラス紀尾井町 19階、20階",
    #             "prefecture": "東京都",
    #             "match_level": 8,
    #             "city": "千代田区",
    #             "town": "紀尾井町",
    #             "town_id": "0056000",
    #             "lg_code": "131016",
    #             "other": "ビル",
    #             "lat": 35.679107172,
    #             "lon": 139.736394597,
    #             "block": "1",
    #             "block_id": "001",
    #             "addr1": "3",
    #             "addr1_id": "003",
    #             "addr2": "3",
    #             "addr2_id": "003"
    #         }
    #     )

    #     mock_service_class.return_value = mock_service_instance

    #     # テスト対象のエンドポイントにリクエストを送信
    #     response = self.app.get('/digital_geocode', query_string={'address': '東京都千代田区紀尾井町1-3'})

        # # ステータスコードとレスポンスの内容を検証
        # self.assertEqual(response.status_code, 200)
        # self.assertIn('data', response.get_data(as_text=True))

        # # モックが呼び出されたことを検証
        # mock_service_instance.return_value.get.assert_called_with('東京都千代田区紀尾井町1-3')


if __name__ == '__main__':
    unittest.main()

