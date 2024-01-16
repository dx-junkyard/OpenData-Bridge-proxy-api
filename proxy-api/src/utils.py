import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import yaml

from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

def get_config(configFileName: str):
    with open(os.path.join('config', configFileName), 'r') as yml:
        config = yaml.safe_load(yml)
    return config

# シークレットを取得する関数
def get_secret(vault_url: str, secret_name: str):
    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=vault_url, credential=credential)
    retrieved_secret = client.get_secret(secret_name)

    return retrieved_secret.value

