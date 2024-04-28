import sys
import os
sys.path.append(
    os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
        'main',
        'DigitalGoGeocode'
    )
)

import json
import unittest
from unittest.mock import patch, MagicMock
from service import DigitalGoGeocodeService, DigitalGoGeocodeDomain

class TestDigitalGoGeocodeService(unittest.TestCase):
    def setUp(self):
        self.service = DigitalGoGeocodeService()
        self.test_address = "東京都新宿区"

    @patch('service.get_secret')
    @patch('service.requests.get')
    def test_get(self, mock_get, mock_get_secret):
        mock_get_secret.return_value = 'https://api.example.com'
        mock_response = MagicMock()
        mock_response.text = json.dumps({
            "lg_code": "123456",
            "town_id": "654321",
            "output": "東京都新宿区西新宿",
            "prefecture": "東京都",
            "city": "新宿区",
            "town": "西新宿",
            "lat": 35.6895,
            "lon": 139.6917
        })
        mock_get.return_value = mock_response
        
        result = self.service.get(self.test_address)
        
        self.assertIsInstance(result, DigitalGoGeocodeDomain)
        self.assertEqual(result.lg_code, "123456")
        self.assertEqual(result.town_id, "654321")
        self.assertEqual(result.fulladdress, "東京都新宿区西新宿")
        self.assertEqual(result.prefecture, "東京都")
        self.assertEqual(result.city, "新宿区")
        self.assertEqual(result.town, "西新宿")
        self.assertEqual(result.lat, 35.6895)
        self.assertEqual(result.lon, 139.6917)
        
        mock_get_secret.assert_called_once_with('digital-go-geocode-url')
        expected_url = 'https://api.example.com/digital_geocode?address=東京都新宿区'
        mock_get.assert_called_once_with(expected_url)

if __name__ == '__main__':
    unittest.main()
