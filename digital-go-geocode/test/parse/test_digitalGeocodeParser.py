import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.parse.digitalGeocdeParser import DigitalGeocdeParser
from src.parse.digitalGeocdeParser import DigitalGeocodeDomain

import unittest

class TestDigitalGeocodeParser(unittest.TestCase):
    # 正常系
    def test_parse(self):
        # テスト用のJSON文字列
        jsonStr = """
        [
            {
                "query": {
                    "input": "東京都千代田区紀尾井町1-3"
                },
                "result": {
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
            }
        ]
        """

        # パーサーのインスタンス化
        parser = DigitalGeocdeParser()

        # パース実行
        result = parser.parse(jsonStr)

        # 結果の検証
        self.assertIsInstance(result, DigitalGeocodeDomain)
        self.assertEqual(result.output, "東京都千代田区紀尾井町1-3 東京ガーデンテラス紀尾井町 19階、20階")
        self.assertEqual(result.prefecture, "東京都")
        self.assertEqual(result.match_level, 8)
        self.assertEqual(result.city, "千代田区")
        self.assertEqual(result.town, "紀尾井町")
        self.assertEqual(result.town_id, "0056000")
        self.assertEqual(result.lg_code, "131016")
        self.assertEqual(result.other, "ビル")
        self.assertAlmostEqual(result.lat, 35.679107172) # 浮動小数点の比較
        self.assertAlmostEqual(result.lon, 139.736394597) # 浮動小数点の比較
        self.assertEqual(result.block, "1")
        self.assertEqual(result.block_id, "001")
        self.assertEqual(result.addr1, "3")
        self.assertEqual(result.addr1_id, "003")
        self.assertEqual(result.addr2, "3")
        self.assertEqual(result.addr2_id, "003")
        
    # 空のパターン
    def test_parse_empty_data(self):
        # テスト用のJSON文字列
        jsonStr = """
        [
            {
            }
        ]
        """

        # パーサーのインスタンス化
        parser = DigitalGeocdeParser()

        # パース実行
        result = parser.parse(jsonStr)

        # 結果の検証
        self.assertIsInstance(result, DigitalGeocodeDomain)
        self.assertEqual(result.output, "")
        self.assertEqual(result.prefecture, "")
        self.assertEqual(result.match_level, 0)
        self.assertEqual(result.city, "")
        self.assertEqual(result.town, "")
        self.assertEqual(result.town_id, "")
        self.assertEqual(result.lg_code, "")
        self.assertEqual(result.other, "")
        self.assertAlmostEqual(result.lat, 0) # 浮動小数点の比較
        self.assertAlmostEqual(result.lon, 0) # 浮動小数点の比較
        self.assertEqual(result.block, "")
        self.assertEqual(result.block_id, "")
        self.assertEqual(result.addr1, "")
        self.assertEqual(result.addr1_id, "")
        self.assertEqual(result.addr2, "")
        self.assertEqual(result.addr2_id, "")

if __name__ == '__main__':
    unittest.main()