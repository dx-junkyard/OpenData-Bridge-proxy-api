import sys
import os
sys.path.append(
    os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
        'main',
        'UniversalMenu'
    )
)

import unittest
from unittest.mock import patch
from service import UniversalMenuService, UniversalMenuDomain

class TestUniversalMenuService(unittest.TestCase):
    def setUp(self):
        self.service = UniversalMenuService()

    @patch('service.UniversalMenuRepository')
    def test_get(self, mock_repository):
        mock_repo_instance = mock_repository.return_value
        mock_repo_instance.getCorporateCode.return_value = '12345'
        mock_repo_instance.getGroupCode.return_value = '67890'
        
        result = self.service.get('Tokyo')
        
        self.assertIsInstance(result, UniversalMenuDomain)
        self.assertEqual(result.corporateCode, '12345')
        self.assertEqual(result.groupCode, '67890')

        mock_repo_instance.getCorporateCode.assert_called_once_with('Tokyo')
        mock_repo_instance.getGroupCode.assert_called_once_with('Tokyo')

if __name__ == '__main__':
    unittest.main()
