import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.parse.digitalGoGeocodeParser import DigitalGoGeocdeParser
from src.parse.digitalGoGeocodeParser import DigitalGoGeocodeDomain

import unittest

class TestDigitalGoGeocodeParser(unittest.TestCase):
    # 正常系
    def test_parse(self):
        # テスト用のJSON文字列
        jsonStr = """
        {
            "addr1": "3",
            "addr1_id": "003",
            "addr2": "",
            "addr2_id": "",
            "block": "1",
            "block_id": "001",
            "city": "千代田区",
            "lat": 35.679107172,
            "lg_code": "131016",
            "lon": 139.736394597,
            "match_level": 8,
            "other": "東京ガーデンテラス紀尾井町 19階、20階",
            "output": "東京都千代田区紀尾井町1-3 東京ガーデンテラス紀尾井町 19階、20階",
            "prefecture": "東京都",
            "town": "紀尾井町",
            "town_id": "0056000"
        }
        """

        # パーサーのインスタンス化
        parser = DigitalGoGeocdeParser()

        # パース実行
        result = parser.parse(jsonStr)

        # 結果の検証
        self.assertIsInstance(result, DigitalGoGeocodeDomain)
        self.assertEqual(result.lg_code, "131016")
        self.assertEqual(result.town_id, "0056000")
        self.assertEqual(result.fulladdress, "東京都千代田区紀尾井町1-3 東京ガーデンテラス紀尾井町 19階、20階")
        self.assertEqual(result.prefecture, "東京都")
        self.assertEqual(result.city, "千代田区")
        self.assertEqual(result.town, "紀尾井町")
        self.assertAlmostEqual(result.lat, 35.679107172)
        self.assertAlmostEqual(result.lon, 139.736394597)
        
    # 空のパターン
    def test_parse_empty_data(self):
        # テスト用のJSON文字列
        jsonStr = """
        {}
        """

        # パーサーのインスタンス化
        parser = DigitalGoGeocdeParser()

        # パース実行
        result = parser.parse(jsonStr)

        # 結果の検証
        self.assertIsInstance(result, DigitalGoGeocodeDomain)
        self.assertEqual(result.lg_code, "")
        self.assertEqual(result.town_id, "")
        self.assertEqual(result.fulladdress, "")
        self.assertEqual(result.prefecture, "")
        self.assertEqual(result.city, "")
        self.assertEqual(result.town, "")
        self.assertAlmostEqual(result.lat, 0)
        self.assertAlmostEqual(result.lon, 0)

if __name__ == '__main__':
    unittest.main()