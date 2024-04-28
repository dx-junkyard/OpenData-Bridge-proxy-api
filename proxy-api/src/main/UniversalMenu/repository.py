import os
import pandas as pd

class UniversalMenuRepository(object):
    def __init__(self):
        self.docsPath = os.path.join(os.path.dirname(__file__), 'resources')
        
    def get(self, city):
        df = pd.read_excel(os.path.join(self.docsPath, 'cities.xlsx'), header=1)
        print(df)

        x = df[df['名称'] == city]

        if not x.empty:
            return x['法人番号'].iloc[0]
        else:
            return None  # 該当する都市が見つからない場合はNoneを返す
        

    def get2(self, city):
        df = pd.read_excel(os.path.join(self.docsPath, '000925835.xls'))
        print(df)

        x = df[df['市区町村名\n（漢字）'] == city]

        if not x.empty:
            return x['団体コード'].iloc[0]
        else:
            return None  # 該当する都市が見つからない場合はNoneを返す


x = UniversalMenuRepository().get2('札幌市')
print(x)