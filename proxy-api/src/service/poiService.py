import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from domain.poiDomain import POIDomain
from repository.poiRepository import POIRepository

class POIService(object):
    def __init__(self):
        self.repository = POIRepository()

    def get(self, word: str) -> POIDomain:
        return self.repository.get(word)
