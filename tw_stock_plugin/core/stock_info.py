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
from tw_stock_plugin.config import Config
from tw_stock_plugin.object.stock_info import StockInfoObject


class StockInfo:
    """
    TODO
        https://dts.twse.com.tw/opendata/t187ap03_L.csv
        https://dts.twse.com.tw/opendata/t187ap03_O.csv
    for getting basic stock info
    """

    def __init__(self):
        self._csv_dir = Config.STOCK_CSV_DIR
        self._stock_data = self._load_stocks()

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
            df['證券代號'] = df['證券代號'].astype(str)
            df = df.fillna('')
            for data in df.values.tolist():
                stock_info = StockInfoObject(*data)
                stocks[stock_info.code] = stock_info
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
