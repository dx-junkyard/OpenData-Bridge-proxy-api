import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import unittest
from unittest.mock import patch
from src.service.digitalGeocodeService import DigitalGeocodeService
from src.service.digitalGeocodeService import DigitalGeocodeDomain

class TestDigitalGeocodeService(unittest.TestCase):
    @patch('subprocess.run')
    def test_get(self, mock_run):
        # 模擬的なsubprocess.runの出力を設定
        mock_run.return_value.stdout = """
        [
            {
                "query": {
                    "input": "東京都千代田区紀尾井町1-3"
                },
                "result": {
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

        # DigitalGeocodeServiceのインスタンスを作成
        service = DigitalGeocodeService()

        # getメソッドをテスト
        result = service.get("東京都千代田区紀尾井町1-3")

        # 結果の検証
        self.assertIsInstance(result, DigitalGeocodeDomain)
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

if __name__ == '__main__':
    unittest.main()
