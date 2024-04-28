import requests
from bs4 import BeautifulSoup

try:
    from domain import Link, ExtractLinks
except:
    from .domain import Link, ExtractLinks
    
class ExtractLinkService(object):
    def get(self, url):
        # URLからページを取得
        response = requests.get(url)
        # BeautifulSoupを使用してHTMLを解析
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # すべての<a>タグを見つける
        links = []
        for tag in soup.find_all('a'):
            # HREF属性とテキストを取得
            href = tag.get('href')
            text = tag.text.strip()
            # Linkデータクラスのインスタンスを作成しリストに追加
            link = Link(href=href, text=text)
            links.append(link)
        
        # Linkのリストを含むExtractLinksを返す
        return ExtractLinks(links=links)