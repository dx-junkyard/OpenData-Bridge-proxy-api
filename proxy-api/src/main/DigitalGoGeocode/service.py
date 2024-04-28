import os
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

import json
import requests

try:
    from domain import DigitalGoGeocodeDomain
except:
    from .domain import DigitalGoGeocodeDomain

# シークレットを取得する関数
def get_secret(secret_name: str):
    vaultUrl = os.getenv('KEY_VAULT_URL')

    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=vaultUrl, credential=credential)
    retrieved_secret = client.get_secret(secret_name)

    return retrieved_secret.value

class DigitalGoGeocodeService(object):
    def get(self, address: str):
        baseUrl = self.getBaseUrl()
        url = f'{baseUrl}/digital_geocode?address={address}'
        response = requests.get(url)

        return self.parse(response.text)

    def getBaseUrl(self):
        return get_secret('digital-go-geocode-url')

    def parse(self, jsonData: str) -> DigitalGoGeocodeDomain:
        data = json.loads(jsonData)

        digitalGeocodeData = {
            "lg_code": data.get("lg_code", ""),
            "town_id": data.get("town_id", ""),
            "fulladdress": data.get("output", ""),
            "prefecture": data.get("prefecture", ""),
            "city": data.get("city", ""),
            "town": data.get("town", ""),
            "lat": data.get("lat", 0),
            "lon": data.get("lon", 0)            
        }

        return DigitalGoGeocodeDomain(**digitalGeocodeData)
