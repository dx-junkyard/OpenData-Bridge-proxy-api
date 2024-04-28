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
from domain import Link, ExtractLinks

class TestDataClasses(unittest.TestCase):
    def test_link_dataclass(self):
        link = Link(href="https://example.com", text="Example")
        
        self.assertEqual(link.href, "https://example.com")
        self.assertEqual(link.text, "Example")
    
    def test_extract_links_dataclass(self):
        links = [
            Link(href="https://example.com", text="Example"),
            Link(href="https://openai.com", text="OpenAI")
        ]
        
        extract_links = ExtractLinks(links=links)
        
        self.assertEqual(len(extract_links.links), 2)
        self.assertEqual(extract_links.links[0].href, "https://example.com")
        self.assertEqual(extract_links.links[0].text, "Example")
        self.assertEqual(extract_links.links[1].href, "https://openai.com")
        self.assertEqual(extract_links.links[1].text, "OpenAI")

if __name__ == '__main__':
    unittest.main()
