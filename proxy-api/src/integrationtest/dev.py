import unittest
from base import IntegrationTest

def load_tests(loader, tests, pattern):
    test_cases = unittest.TestSuite()
    url = "https://dev-fukumoto.azurewebsites.net/api"

    # クラス変数を直接設定
    IntegrationTest.setTargetUrl(url)

    # クラスからテストをロード
    loaded_tests = loader.loadTestsFromTestCase(IntegrationTest)
    test_cases.addTests(loaded_tests)

    return test_cases
if __name__ == '__main__':
    unittest.main()