import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.domain.poiDomain import POIDomain

import pandas as pd
import logging

class POIRepository(object):
    def __init__(self):
        # Excelファイルのパス
        file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'resources', 'poi', '491-3-1_POIコード表.xlsx')
        logging.info(file_path)
        # Excelファイルを読み込む
        self.df = pd.read_excel(file_path, header=1)

    def get(self, word: str) -> str:
        df = self.df

        # 複数の列における特定の文字列の出現回数をカウントする関数
        def count_occurrences_in_columns(row, columns, word):
            # NaNを無視してカウントする
            return sum(row[col].count(word) for col in columns if pd.notna(row[col]))

        # 対象の列と文字列を指定
        columns_to_count = ['解説', '対象']
        word_to_count = word

        # 各行について選択した列の合計出現回数を計算し、新しい列に保存
        df['total_count'] = df.apply(lambda row: count_occurrences_in_columns(row, columns_to_count, word_to_count), axis=1)

        # 合計出現回数でソート
        sorted_df = df.sort_values(by='total_count', ascending=False)

        return POIDomain(sorted_df.iloc[0]['コード'])