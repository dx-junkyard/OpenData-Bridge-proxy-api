import os
import uuid
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

import json
import requests

try:
    from domain import TranslateJpToEnDomain
except:
    from .domain import TranslateJpToEnDomain

# シークレットを取得する関数
def get_secret(secret_name: str):
    vaultUrl = os.getenv('KEY_VAULT_URL')

    print(vaultUrl)

    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=vaultUrl, credential=credential)
    retrieved_secret = client.get_secret(secret_name)

    return retrieved_secret.value

class TranslateJpToEnService(object):
    def get(self, jp):
        headers = {
            'Ocp-Apim-Subscription-Key': get_secret('TRANSLATE-API-KEY'), # TODO
            'Ocp-Apim-Subscription-Region': 'japaneast',
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }
        
        body = [{'text': jp}]

        AZURE_TRANSLATOR_URL = get_secret('AZURE-TRANSLATOR-URL')
        url = f'{AZURE_TRANSLATOR_URL}/translate?api-version=3.0&from=ja&to=en'

        response = requests.post(url, headers=headers, json=body)

        return self.parse(response.text)

    def parse(self, jsonData: str) -> TranslateJpToEnDomain:
        data = json.loads(jsonData)

        jp2enData = {
            'en': data[0]['translations'][0]['text'] if len(data) > 0 and "translations" in data[0] else ''
        }

        return TranslateJpToEnDomain(**jp2enData)
