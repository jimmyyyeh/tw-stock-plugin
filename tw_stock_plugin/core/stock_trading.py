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
from datetime import date

from tw_stock_plugin.core.stock_tools import StockTools
from tw_stock_plugin.object.stock_trading import TwseTradingObject, TpexTradingObject
from tw_stock_plugin.constant import Domain
from tw_stock_plugin.utils.response_handler import ResponseHandler


class StockTrading:
    def __init__(self, date_):
        """
        :param date_: 查詢日期
        """
        self.date_ = date_
        self.trading_dict = dict()
        self._valid_date()

    def _valid_date(self):
        """
        valid date format
        """
        if not isinstance(self.date_, date):
            raise TypeError('input date must be type of datetime.date')

    def _fetch_twse_data_all(self):
        """
        fetch all trading data in specific date from twse website
        :return:
        """
        url = f'{Domain.TAIWAN_STOCK_EXCHANGE_CORPORATION}/exchangeReport/MI_INDEX'
        query_date = self.date_.strftime('%Y%m%d')
        params = {
            'response': 'json',
            'date': query_date,
            'type': 'ALL'
        }
        response = ResponseHandler.get(url=url, params=params)
        if not response:
            raise ValueError(f'{self.date_} result not found')
        json_data = response.json()
        data_list = json_data['data9']
        for data in data_list:
            stock_trading = TwseTradingObject(*data)
            self.trading_dict[stock_trading.code] = stock_trading

    def _fetch_tpex_data_all(self):
        """
        fetch all trading data in specific date from tpex website
        :return:
        """
        url = f'{Domain.TAIPEI_EXCHANGE}/web/stock/aftertrading/otc_quotes_no1430/stk_wn1430_result.php'
        query_date = StockTools.ad_to_republic_era(date_=self.date_).replace('-', '/'),
        params = {
            'l': 'zh-tw',
            'd': query_date,
            'se': 'EW'
        }
        response = ResponseHandler.get(url=url, params=params)
        if not response:
            raise ValueError(f'{self.date_} result not found')
        json_data = response.json()
        data_list = json_data['aaData']
        for data in data_list:
            stock_trading = TpexTradingObject(*data)
            self.trading_dict[stock_trading.code] = stock_trading

    def get_all(self):
        """
        return all trading data
        :return:
        """
        self._fetch_twse_data_all()
        self._fetch_tpex_data_all()
        return self.trading_dict
