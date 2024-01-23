from azure.storage.blob import BlobServiceClient
import logging

class BlobRepository(object):
    def __init__(self, connect_str: str, container_name: str, blob_name: str):
        # BlobServiceClientの初期化
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)

        # BlobClientの取得
        self.blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

    def get(self) -> str:
        try:
            return self.blob_client.download_blob().readall().decode()
        except Exception as e:
            logging.error(e)
        return None

    def update(self, data: str):
        try:
            self.blob_client.upload_blob(data.encode(), overwrite=True)
        except Exception as e:
            logging.error(e)
