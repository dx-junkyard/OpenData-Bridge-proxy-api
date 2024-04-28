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
from unittest.mock import MagicMock
from service import SwaggerService

class TestSwaggerService(unittest.TestCase):
    def setUp(self):
        self.service = SwaggerService()
        self.mock_repository = MagicMock()
        self.original_repository = self.service.repository
        self.service.repository = self.mock_repository

    def tearDown(self):
        SwaggerService.repository = self.original_repository

    def test_get_ui(self):
        self.mock_repository.getUi.return_value = 'mock_ui'
        
        result = self.service.getUi()
        
        self.assertEqual(result, 'mock_ui')
        self.mock_repository.getUi.assert_called_once()

    def test_get_json(self):
        self.mock_repository.getJson.return_value = 'mock_json'
        
        result = self.service.getJson()
        
        self.assertEqual(result, 'mock_json')
        self.mock_repository.getJson.assert_called_once()

if __name__ == '__main__':
    unittest.main()
