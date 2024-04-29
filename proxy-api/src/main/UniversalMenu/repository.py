import os
import pandas as pd

class UniversalMenuRepository(object):
    def __init__(self):
        self.docsPath = os.path.join(os.path.dirname(__file__), 'resources')
        
    def getCorporateCode(self, city):
        df = pd.read_excel(os.path.join(self.docsPath, 'cities.xlsx'), header=1, dtype=str)

        df_ = df[df['名称'] == city]

        if not df_.empty:
            return df_['法人番号'].iloc[0]
        else:
            return ""

    def getGroupCode(self, city):
        df = pd.read_excel(os.path.join(self.docsPath, '000925835.xls'), dtype=str)

        df_ = df[df['市区町村名\n（漢字）'] == city]

        if not df_.empty:
            return df_['団体コード'].iloc[0]
        else:
            return ""
