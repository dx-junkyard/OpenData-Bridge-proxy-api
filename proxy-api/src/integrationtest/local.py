import unittest
from base import IntegrationTest

def load_tests(loader, tests, pattern):
    test_cases = unittest.TestSuite()
    url = "http://localhost:7071/api"

    test_class = IntegrationTest()
    test_class.set_target_url(url)
    loaded_tests = loader.loadTestsFromTestCase(type(test_class))
    test_cases.addTests(loaded_tests)

    return test_cases

if __name__ == '__main__':
    unittest.main()