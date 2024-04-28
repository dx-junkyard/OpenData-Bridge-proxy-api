import sys
import os
sys.path.append(
    os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
        'main',
        'ExtractLinks'
    )
)
import unittest
from unittest.mock import patch, MagicMock
from service import ExtractLinkService, ExtractLinks

class TestExtractLinkService(unittest.TestCase):
    def setUp(self):
        self.service = ExtractLinkService()
        self.test_url = "https://example.com"

    @patch('service.requests.get')
    @patch('service.BeautifulSoup')
    def test_get(self, mock_beautiful_soup, mock_requests_get):
        mock_response = MagicMock()
        mock_response.text = '''
            <html>
                <body>
                    <a href="https://example.com" text="Example">Example Link</a>
                    <a href="https://example2.com" text="Example2">Second Link</a>
                </body>
            </html>
        '''
        mock_requests_get.return_value = mock_response
        
        mock_tag1 = MagicMock()
        mock_tag1.get.side_effect = lambda x: "https://example.com" if x == "href" else "Example Link"
        mock_tag1.text = "Example Link"
        
        mock_tag2 = MagicMock()
        mock_tag2.get.side_effect = lambda x: "https://example2.com" if x == "href" else "Second Link"
        mock_tag2.text = "Second Link"

        mock_soup = MagicMock()
        mock_soup.find_all.return_value = [mock_tag1, mock_tag2]
        mock_beautiful_soup.return_value = mock_soup

        result = self.service.get(self.test_url)
        
        self.assertIsInstance(result, ExtractLinks)
        self.assertEqual(len(result.links), 2)
        self.assertEqual(result.links[0].href, "https://example.com")
        self.assertEqual(result.links[0].text, "Example Link")
        self.assertEqual(result.links[1].href, "https://example2.com")
        self.assertEqual(result.links[1].text, "Second Link")
        
        mock_requests_get.assert_called_once_with(self.test_url)
        mock_beautiful_soup.assert_called_once_with(mock_response.text, 'html.parser')
        mock_soup.find_all.assert_called_once_with('a')

if __name__ == '__main__':
    unittest.main()
