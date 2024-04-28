import sys
import os
sys.path.append(
    os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
        'main',
        'TranslateJpToEn'
    )
)
from domain import TranslateJpToEnDomain

import unittest

class TestTranslateJpToEnDomain(unittest.TestCase):

    def test_initialization(self):
        # テストデータの準備
        test_data = {
            "en": "test",
        }

        # データクラスのインスタンス化
        domain = TranslateJpToEnDomain(**test_data)

        # 各属性が正しく設定されていることを検証
        for key, value in test_data.items():
            self.assertEqual(getattr(domain, key), value)

# テストの実行
if __name__ == '__main__':
    unittest.main()