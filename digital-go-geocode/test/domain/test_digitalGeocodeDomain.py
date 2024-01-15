import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.domain.digitalGeocodeDomain import DigitalGeocodeDomain

import unittest

class TestDigitalGeocodeDomain(unittest.TestCase):

    def test_initialization(self):
        # テストデータの準備
        test_data = {
            "output": "東京都千代田区紀尾井町1-3 東京ガーデンテラス紀尾井町 19階、20階",
            "prefecture": "東京都",
            "match_level": 8,
            "city": "千代田区",
            "town": "紀尾井町",
            "town_id": "0056000",
            "lg_code": "131016",
            "other": "",
            "lat": 35.679107172,
            "lon": 139.736394597,
            "block": "1",
            "block_id": "001",
            "addr1": "3",
            "addr1_id": "003",
            "addr2": "",
            "addr2_id": ""
        }

        # データクラスのインスタンス化
        domain = DigitalGeocodeDomain(**test_data)

        # 各属性が正しく設定されていることを検証
        for key, value in test_data.items():
            self.assertEqual(getattr(domain, key), value)

# テストの実行
if __name__ == '__main__':
    unittest.main()