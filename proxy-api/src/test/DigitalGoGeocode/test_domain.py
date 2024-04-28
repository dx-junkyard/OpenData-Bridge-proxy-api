import sys
import os
sys.path.append(
    os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
        'main',
        'DigitalGoGeocode'
    )
)

from domain import DigitalGoGeocodeDomain

import unittest

class TestDigitalGoGeocodeDomain(unittest.TestCase):

    def test_initialization(self):
        # テストデータの準備
        test_data = {
            "lg_code": "131016",
            "town_id": "0056000",
            "fulladdress": "東京都千代田区紀尾井町1-3 東京ガーデンテラス紀尾井町 19階、20階",
            "prefecture": "東京都",
            "city": "千代田区",
            "town": "紀尾井町",
            "lat": 35.679107172,
            "lon": 139.736394597,
        }

        # データクラスのインスタンス化
        domain = DigitalGoGeocodeDomain(**test_data)

        # 各属性が正しく設定されていることを検証
        for key, value in test_data.items():
            self.assertEqual(getattr(domain, key), value)

# テストの実行
if __name__ == '__main__':
    unittest.main()