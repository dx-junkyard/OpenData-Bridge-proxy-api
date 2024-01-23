import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.parse.jp2enParser import jp2enParser
from src.parse.jp2enParser import jp2enDomain

import unittest

class Tesjp2enParser(unittest.TestCase):
    # 正常系
    def test_parse(self):
        # テスト用のJSON文字列
        jsonStr = '[{"translations":[{"text":"Tokyo","to":"en"}]}]'

        # パーサーのインスタンス化
        parser = jp2enParser()

        # パース実行
        result = parser.parse(jsonStr)

        # 結果の検証
        self.assertIsInstance(result, jp2enDomain)
        self.assertEqual(result.en, "Tokyo")

    # 空のパターン
    def test_parse_empty_data(self):
        # テスト用のJSON文字列
        jsonStr = "[]"

        # パーサーのインスタンス化
        parser = jp2enParser()

        # パース実行
        result = parser.parse(jsonStr)

        # 結果の検証
        self.assertIsInstance(result, jp2enDomain)
        self.assertEqual(result.en, "")

if __name__ == '__main__':
    unittest.main()