import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import logging
import requests

from parse.digitalGoGeocodeParser import DigitalGoGeocdeParser
from domain.digitalGoGeocodeDomain import DigitalGoGeocodeDomain
from utils import get_secret

class DigitalGoGeocodeService(object):
    def __init__(self, key_vault_url, config):
        self.parser = DigitalGoGeocdeParser()
        self._URL = get_secret(key_vault_url, config['secret-name'])

    def get(self, address: str) -> DigitalGoGeocodeDomain:
        path = '/digital_geocode'
        params = f'?address={address}'  # 日本語から英語への翻訳
        constructed_url = self._URL + path + params
        response = requests.get(constructed_url)

        return self.parser.parse(response.text)
