import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from domain.jp2enDomain import jp2enDomain

import json

class jp2enParser:
    def parse(self, jsonStr: str) -> jp2enDomain:
        data = json.loads(jsonStr)

        jp2enData = {
            'en': data[0]['translations'][0]['text'] if len(data) > 0 and "translations" in data[0] else ''
        }

        return jp2enDomain(**jp2enData)

