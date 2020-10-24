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
import glob
import pandas as pd

from tw_stock_plugin import UpdateStock
from tw_stock_plugin._config import Config


class StockPlugin:
    class Stock:
        def __init__(self, code, name, ISIN_code, listed_date, category, industry, CFI_code):
            """
            :param code: 股票代碼
            :param name: 股票名稱
            :param ISIN_code: 國際證券辨識號碼(ISIN Code)
            :param listed_date: 上市/上櫃/興櫃 日
            :param category: 市場別
            :param industry: 產業別
            :param CFI_code: CFICode
            """
            self.code = code
            self.name = name
            self.ISIN_code = ISIN_code
            self.listed_date = listed_date
            self.category = category
            self.industry = industry
            self.CFI_code = CFI_code

    def __init__(self):
        self._stock_data = self._load_stocks()
        self._csv_dir = Config.STOCK_CSV_DIR

    def _get_stock_csv_files(self):
        """
        check if csv files exists, if so, return csv files, else, crawling data from website
        :return:
        """
        if not (os.path.isdir(self._csv_dir) and len(os.listdir(self._csv_dir)) == 3):
            UpdateStock.main()
        return glob.glob(f'{self._csv_dir}/*.csv')

    def _load_stocks(self):
        """
        init stock data when object created
        :return:
        """
        stocks = dict()
        csv_files = self._get_stock_csv_files()
        for csv in csv_files:
            df = pd.read_csv(csv, index_col=0)
            for data in df.values.tolist():
                stock = self.Stock(*data)
                stocks[stock.code] = stock
        return stocks

    def get(self, code=None):
        """
        get stock data by stock code
        :param code:
        :return:
        """
        if code:
            if code not in self._stock_data:
                raise ValueError('stock code not exists')
            return self._stock_data[code]
        else:
            return self._stock_data


if __name__ == '__main__':
    print(StockPlugin().get())
    print(StockPlugin().get('1101'))
    print(StockPlugin().get('1101').name)
    print(StockPlugin().get('1101 B'))
