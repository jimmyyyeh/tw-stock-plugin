# -*- coding: utf-8 -*
"""
      ┏┓       ┏┓
    ┏━┛┻━━━━━━━┛┻━┓
    ┃      ☃      ┃
    ┃  ┳┛     ┗┳  ┃
    ┃      ┻      ┃
    ┗━┓         ┏━┛
      ┗┳        ┗━┓
       ┃          ┣┓
       ┃          ┏┛
       ┗┓┓┏━━━━┳┓┏┛
        ┃┫┫    ┃┫┫
        ┗┻┛    ┗┻┛
    God Bless,Never Bug
"""

import os
import re
import requests
import pandas as pd
from time import sleep

from tw_stock_plugin._config import Config


class UpdateStock:
    _URL_DICT = {
        'stock_exchange': 'https://isin.twse.com.tw/isin/C_public.jsp?strMode=2',
        'over_the_counter': 'https://isin.twse.com.tw/isin/C_public.jsp?strMode=4',
        'emerging_stock': 'https://isin.twse.com.tw/isin/C_public.jsp?strMode=5'
    }

    _CODE_NAME_PATTERN = re.compile(r'[\da-zA-Z]+\s.*')

    @staticmethod
    def _get_response(url):
        """
        :param url:
        :return:
        """
        response = requests.get(url)
        return response

    @classmethod
    def main(cls):
        """
        :return:
        """
        # create csv dir if dir not exists
        if not os.path.isdir(Config.STOCK_CSV_DIR):
            os.mkdir(Config.STOCK_CSV_DIR)

        print('UPDATING STOCK INFO')
        for category, url in cls._URL_DICT.items():
            response = cls._get_response(url=url)
            df = pd.read_html(response.text)[0]
            df_columns = df.iloc[0]
            new_data = [data for data in df.values.tolist() if cls._CODE_NAME_PATTERN.search(data[0])]
            df = pd.DataFrame(new_data, columns=df_columns)
            code_name_df = pd.DataFrame(df['有價證券代號及名稱'].str.split('\u3000', 1).tolist(),
                                        columns=['證券代號', '證券名稱'])
            df = df.drop(['有價證券代號及名稱', '備註'], axis=1)
            df = pd.concat([code_name_df, df], axis=1)
            csv_path = os.path.join(Config.STOCK_CSV_DIR, f'{category}.csv')
            df.to_csv(csv_path)
            # to avoiding banned by twse website
            sleep(3)
        print('FINISHED')


if __name__ == '__main__':
    UpdateStock.main()
