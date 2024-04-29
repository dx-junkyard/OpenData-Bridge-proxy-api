import sys
import os
sys.path.append(
    os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
        'main',
        'UniversalMenu'
    )
)
import pandas as pd
import unittest
from unittest.mock import patch
from repository import UniversalMenuRepository

class TestUniversalMenuRepository(unittest.TestCase):
    def setUp(self):
        self.repo = UniversalMenuRepository()

    @patch('repository.pd.read_excel')
    def test_get_corporate_code_found(self, mock_read_excel):
        mock_df = pd.DataFrame({
            '名称': ['東京', '大阪'],
            '法人番号': ['12345', '67890']
        })
        mock_read_excel.return_value = mock_df

        result = self.repo.getCorporateCode('東京')
        
        self.assertEqual(result, '12345')

    @patch('repository.pd.read_excel')
    def test_get_corporate_code_not_found(self, mock_read_excel):
        mock_df = pd.DataFrame({
            '名称': ['東京', '大阪'],
            '法人番号': ['12345', '67890']
        })
        mock_read_excel.return_value = mock_df

        result = self.repo.getCorporateCode('京都')
        
        self.assertEqual(result, '')

    @patch('repository.pd.read_excel')
    def test_get_group_code_found(self, mock_read_excel):
        mock_df = pd.DataFrame({
            '市区町村名\n（漢字）': ['東京', '大阪'],
            '団体コード': ['11111', '22222']
        })
        mock_read_excel.return_value = mock_df

        result = self.repo.getGroupCode('東京')
        
        self.assertEqual(result, '11111')

    @patch('repository.pd.read_excel')
    def test_get_group_code_not_found(self, mock_read_excel):
        mock_df = pd.DataFrame({
            '市区町村名\n（漢字）': ['東京', '大阪'],
            '団体コード': ['11111', '22222']
        })
        mock_read_excel.return_value = mock_df

        result = self.repo.getGroupCode('京都')
        
        self.assertEqual(result, '')

if __name__ == '__main__':
    unittest.main()
