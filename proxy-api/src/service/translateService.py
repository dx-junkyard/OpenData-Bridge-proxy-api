import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import uuid
import requests
import logging
from parse.jp2enParser import jp2enParser
from utils import get_secret

class TranslateService(object):
    def __init__(self):
        self.parser = jp2enParser()
        SECRET_NAME = "DataNorm-Translator"
        self._API_KEY = get_secret(SECRET_NAME) # APIキーのシークレット名を指定
        self._ENDPOINT = "https://api.cognitive.microsofttranslator.com/"
        
    def jp2en(self, jp_str):
        headers = {
            'Ocp-Apim-Subscription-Key': self._API_KEY,
            'Ocp-Apim-Subscription-Region': 'japaneast',
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }
        
        body = [{'text': jp_str}]

        path = '/translate?api-version=3.0'
        params = '&from=ja&to=en'  # 日本語から英語への翻訳
        constructed_url = self._ENDPOINT + path + params

        response = requests.post(constructed_url, headers=headers, json=body)

        return self.parser.parse(response.text)


