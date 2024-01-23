import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.repository.blobRepository import BlobRepository
from domain.idDomain import IDDomain
from utils import get_secret
import logging
class IDService(object):
    def __init__(self, key_vault_url, config):
        connect_str = get_secret(key_vault_url, config['azure-storage']['secret-name']) # APIキーのシークレット名を指定
        container_name = config['azure-storage']['container-name']
        blob_name = config['azure-storage']['blob-name']

        self.blobRepository = BlobRepository(connect_str, container_name, blob_name)
        
    def get(self, header='') -> IDDomain:
        Id = self.blobRepository.get()
        if Id is None: Id = '0'

        self.blobRepository.update(str(int(Id)+1))
        return IDDomain(header + Id)

    def reset(self):
        self.blobRepository.update('0')
