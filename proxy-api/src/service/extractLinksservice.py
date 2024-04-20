import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import requests
from bs4 import BeautifulSoup
import json

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
            # JSONに適した辞書形式でリンクを保存
            links.append({'href': href, 'text': text})
        
        # リンクのリストをJSON形式で出力
        return json.dumps(links, ensure_ascii=False)
