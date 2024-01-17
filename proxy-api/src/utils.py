import os
import yaml

from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

def get_config(configFileName: str):
    # 現在のスクリプトファイル（utils.py）の絶対パスを取得
    base_path = os.path.dirname(os.path.abspath(__file__))

    # 'config' ディレクトリと configFileName を絶対パスに追加
    config_path = os.path.join(base_path, '..', 'config', configFileName)

    # 設定ファイルを開いて読み込む
    with open(config_path, 'r') as yml:
        config = yaml.safe_load(yml)

    return config

# シークレットを取得する関数
def get_secret(vault_url: str, secret_name: str):
    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=vault_url, credential=credential)
    retrieved_secret = client.get_secret(secret_name)

    return retrieved_secret.value

