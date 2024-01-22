import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.domain.idDomain import IDDomain

import unittest

class TestIDDomain(unittest.TestCase):

    def test_initialization(self):
        # テストデータの準備
        test_data = {
            "id": "xxx0001",
        }

        # データクラスのインスタンス化
        domain = IDDomain(**test_data)

        # 各属性が正しく設定されていることを検証
        for key, value in test_data.items():
            self.assertEqual(getattr(domain, key), value)

# テストの実行
if __name__ == '__main__':
    unittest.main()