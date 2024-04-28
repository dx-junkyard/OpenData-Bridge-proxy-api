import sys
import os
sys.path.append(
    os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
        'main',
        'Swagger'
    )
)
import unittest
from unittest.mock import patch, mock_open
from repository import SwaggerRepository

class TestSwaggerRepository(unittest.TestCase):
    def setUp(self):
        self.repository = SwaggerRepository()

    @patch('builtins.open', new_callable=mock_open, read_data='<html>...</html>')
    def test_get_ui(self, mock_file):
        result = self.repository.getUi()
        self.assertEqual(result, '<html>...</html>')
        mock_file.assert_called_once_with(os.path.join(self.repository.docsPath, 'index.html'), 'r', encoding='utf-8')

    @patch('builtins.open', new_callable=mock_open, read_data='{"info": "test"}')
    @patch('json.load', return_value={"info": "test"})
    def test_get_json(self, mock_json, mock_file):
        result = self.repository.getJson()
        self.assertEqual(result, {"info": "test"})
        mock_file.assert_called_once_with(os.path.join(self.repository.docsPath, 'openapi.json'), 'r', encoding='utf-8')

if __name__ == '__main__':
    unittest.main()
