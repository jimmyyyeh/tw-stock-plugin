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
import requests
import pandas as pd
from time import sleep

from tw_stock_plugin.config import Config
from tw_stock_plugin.constant import Domain
from tw_stock_plugin.regex_pattern import StockPattern
from tw_stock_plugin.utils.response_handler import ResponseHandler


class UpdateStock:
    _STR_MODE_DICT = {
        'stock_exchange': 2,
        'over_the_counter': 4,
        'emerging_stock': 5
    }

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
        for category, str_mode in cls._STR_MODE_DICT.items():
            params = {
                'strMode': str_mode
            }
            response = ResponseHandler.get(url=f'{Domain.TAIWAN_STOCK_EXCHANGE_CORPORATION_ISIN}/isin/C_public.jsp',
                                           params=params)

            df = pd.read_html(response.text)[0]
            df_columns = df.iloc[0].values.tolist() + ['類別']
            new_data = list()
            tmp_type = None
            for data in df.values.tolist()[1:]:
                if not StockPattern.CODE_NAME_PATTERN.search(data[0]) and len(set(data)) == 1:
                    tmp_type = data[0]
                elif StockPattern.CODE_NAME_PATTERN.search(data[0]):
                    data.append(tmp_type)
                    new_data.append(data)
            df = pd.DataFrame(new_data, columns=df_columns)
            df['有價證券代號及名稱'] = df['有價證券代號及名稱'].apply(lambda x: x.replace('\u3000', ' '))
            code_name_df = pd.DataFrame(df['有價證券代號及名稱'].str.split(' ', 1).tolist(),
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
