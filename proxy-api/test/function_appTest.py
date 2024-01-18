import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ['ConfigFileName'] = 'local.yaml'
import json
from dataclasses import asdict

from src.utils import get_config
import azure.functions as func
from function_app import hello
from function_app import japanese_to_english

from src.domain.jp2enDomain import jp2enDomain


import requests
import unittest
from unittest.mock import Mock, patch

class AppTests(unittest.TestCase):
    config: dict
    KEY_VAULT_URL: str

    @classmethod
    def setUpClass(cls):
        config = get_config('local.yaml')
        cls.KEY_VAULT_URL = config['key-vault']['url']
        cls.config = config
    
    def test_hello_function(self):
        # HttpRequestオブジェクトの作成
        req = func.HttpRequest(
            method='GET',
            url='/hello',
            body=None,
            headers={}
        )

        func_call = hello.build().get_user_function()
        response = func_call(req)
        self.assertEqual(response.status_code, 200)

    @patch('function_app.TranslateService')
    def test_my_function(self, mock_translate_service):
        expected = jp2enDomain(**{"en": "test"})
        mock_translate_service.return_value.jp2en.return_value = expected
        
        req = func.HttpRequest(
            method='GET',
            url='/japanese-to-english',
            body={},
            headers={},
            params={"jp": "テスト"}
        )

        func_call = japanese_to_english.build().get_user_function()
        response = func_call(req)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers.get("Content-Type"), "application/json")
        self.assertIn(json.dumps(asdict(expected)), response.get_body().decode())
        mock_translate_service.assert_called_once_with(AppTests.KEY_VAULT_URL, AppTests.config['azure-translator'])
        mock_translate_service.return_value.jp2en.assert_called_once_with("テスト")

        # TODO MagicMockの方にしたい

if __name__ == '__main__':
    unittest.main()
