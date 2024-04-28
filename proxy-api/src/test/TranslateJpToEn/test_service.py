import sys
import os
sys.path.append(
    os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
        'main',
        'TranslateJpToEn'
    )
)
import json
import unittest
from unittest.mock import patch, MagicMock
from service import TranslateJpToEnService
from domain import TranslateJpToEnDomain

class TestTranslateJpToEnService(unittest.TestCase):
    def setUp(self):
        self.service = TranslateJpToEnService()
        self.test_jp_text = "こんにちは"
        self.test_en_text = "Hello"

    @patch('service.get_secret')
    @patch('requests.post')
    def test_get(self, mock_post, mock_get_secret):
        # シークレット取得のモック設定
        mock_get_secret.side_effect = lambda x: 'mocked_secret' if x == 'TRANSLATE-API-KEY' else 'mocked_url'
        # API応答のモック設定
        mock_response = MagicMock()
        mock_response.text = json.dumps([{'translations': [{'text': self.test_en_text}]}])
        mock_post.return_value = mock_response

        # 翻訳メソッドの実行
        result = self.service.get(self.test_jp_text)
        
        # 結果の検証
        self.assertIsInstance(result, TranslateJpToEnDomain)
        self.assertEqual(result.en, self.test_en_text)

        # get_secretが適切に呼ばれたか確認
        mock_get_secret.assert_any_call('TRANSLATE-API-KEY')
        mock_get_secret.assert_any_call('AZURE-TRANSLATOR-URL')
        
        # requests.postが正しいパラメータで呼ばれたか確認
        mock_post.assert_called_once()

if __name__ == '__main__':
    unittest.main()
