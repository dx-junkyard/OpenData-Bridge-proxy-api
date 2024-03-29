import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from src.service.digitalGoGeocodeService import DigitalGoGeocodeService
from src.utils import get_config

import unittest
from unittest.mock import patch, MagicMock

class TestDigitalGoGeocodeService(unittest.TestCase):
    config: dict
    KEY_VAULT_URL: str

    @classmethod
    def setUpClass(cls):
        config = get_config('local.yaml')
        cls.KEY_VAULT_URL = config['key-vault']['url']
        cls.config = config['digital-go-geocode']

    @patch('src.service.digitalGoGeocodeService.DigitalGoGeocdeParser')
    @patch('src.service.digitalGoGeocodeService.requests.get')
    @patch('src.service.digitalGoGeocodeService.get_secret')
    def test_get(self, mock_get_secret, mock_requests_get, mock_parser_class):
        mock_get_secret.return_value = 'http://test'
        mock_requests_get.return_value = MagicMock(text='')
        mock_parser_class.parse.return_value = MagicMock()

        service = DigitalGoGeocodeService(TestDigitalGoGeocodeService.KEY_VAULT_URL, TestDigitalGoGeocodeService.config)

        service.get("test")

        expected_url = 'http://test/digital_geocode?address=test'

        mock_get_secret.assert_called_once()
        mock_requests_get.assert_called_once_with(expected_url)
        mock_parser_class.assert_called_once()

if __name__ == '__main__':
    unittest.main()
