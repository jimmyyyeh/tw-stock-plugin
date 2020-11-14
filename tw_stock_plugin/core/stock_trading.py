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
from datetime import datetime, date

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
        trading_dict = dict()
        url = f'{Domain.TAIWAN_STOCK_EXCHANGE_CORPORATION}/exchangeReport/MI_INDEX'
        query_date = self.date_.strftime('%Y%m%d')
        params = {
            'response': 'json',
            'date': query_date,
            'type': 'ALL'
        }
        response = ResponseHandler.get(url=url, params=params)
        if not response:
            return None
        json_data = response.json()
        stats = json_data['stat']
        if not stats == 'OK':
            return None
        data_list = json_data['data9']
        columns = ['code', 'name', 'trading_volume', 'transaction', 'trade_value', 'opening_price', 'highest_price',
                   'lowest_price', 'closing_price', 'different', 'change', 'last_best_bid_price',
                   'last_best_bid_volume', 'last_best_ask_price', 'last_best_ask_volume', 'price_earning_rate']
        for data in data_list:
            stock_trading = TwseTradingObject(**dict(zip(columns, data)))
            trading_dict[stock_trading.code] = stock_trading
        return trading_dict

    def _fetch_tpex_data_all(self):
        """
        fetch all trading data in specific date from tpex website
        :return:
        """
        trading_dict = dict()
        url = f'{Domain.TAIPEI_EXCHANGE}/web/stock/aftertrading/otc_quotes_no1430/stk_wn1430_result.php'
        query_date = StockTools.ad_to_republic_era(date_=self.date_).replace('-', '/'),
        params = {
            'l': 'zh-tw',
            'd': query_date,
            'se': 'EW'
        }
        response = ResponseHandler.get(url=url, params=params)
        if not response:
            return None
        json_data = response.json()
        data_list = json_data['aaData']
        if not data_list:
            return None
        columns = ['code', 'name', 'closing_price', 'change', 'opening_price', 'highest_price', 'lowest_price',
                   'trading_volume', 'trade_value', 'transaction', 'last_best_bid_price', 'last_best_bid_volume',
                   'last_best_ask_price', 'last_best_ask_volume', 'issued_shares', 'next_limit_up', 'next_limit_down']
        for data in data_list:
            stock_trading = TpexTradingObject(**dict(zip(columns, data)))
            trading_dict[stock_trading.code] = stock_trading
        return trading_dict

    def get_all(self):
        """
        return all trading data
        :return:
        """
        trading_dict = dict()
        twse_data = self._fetch_twse_data_all()
        tpex_data = self._fetch_tpex_data_all()
        if twse_data:
            trading_dict.update(twse_data)
        if tpex_data:
            trading_dict.update(tpex_data)
        return trading_dict

    def _fetch_twse_data_history(self, code):
        """
        get specific stock monthly trading data from twse website
        :param code:
        :return:
        """
        trading_dict = dict()
        url = f'{Domain.TAIWAN_STOCK_EXCHANGE_CORPORATION}/exchangeReport/STOCK_DAY'
        query_date = self.date_.strftime('%Y%m%d')
        params = {
            'response': 'json',
            'date': query_date,
            'stockNo': code
        }
        response = ResponseHandler.get(url=url, params=params)
        if not response:
            return None
        json_data = response.json()
        stats = json_data['stat']
        if not stats == 'OK':
            return None
        data_list = json_data['data']
        columns = ['trading_volume', 'trade_value', 'opening_price', 'highest_price', 'lowest_price',
                   'closing_price', 'change', 'transaction']

        for data in data_list:
            date_ = StockTools.republic_era_to_ad(data[0])
            date_ = datetime.strptime(date_, '%Y/%m/%d').date()
            stock_trading = TwseTradingObject(**(dict(zip(columns, data[1:]))))
            for attr in stock_trading.__dict__.copy():
                if attr not in columns:
                    delattr(stock_trading, attr)
            trading_dict[date_] = stock_trading
        return trading_dict

    def _fetch_tpex_data_history(self, code):
        trading_dict = dict()
        url = f'{Domain.TAIPEI_EXCHANGE}/web/stock/aftertrading/daily_trading_info/st43_result.php'
        query_date = StockTools.ad_to_republic_era(date_=self.date_).replace('-', '/'),
        params = {
            'l': 'zh-tw',
            'd': query_date,
            'stkno': code
        }
        response = ResponseHandler.get(url=url, params=params)
        if not response:
            return None
        json_data = response.json()
        data_list = json_data['aaData']
        if not data_list:
            return None
        columns = ['trading_volume', 'trade_value', 'opening_price', 'highest_price', 'lowest_price',
                   'closing_price', 'change', 'transaction']
        for data in data_list:
            date_ = StockTools.republic_era_to_ad(data[0])
            date_ = datetime.strptime(date_, '%Y/%m/%d').date()
            stock_trading = TpexTradingObject(**(dict(zip(columns, data[1:]))))
            for attr in stock_trading.__dict__.copy():
                if attr not in columns:
                    delattr(stock_trading, attr)
            trading_dict[date_] = stock_trading
        return trading_dict

    def get_history(self, code):
        """
        return monthly trading data with specific stock code
        :param code:
        :return:
        """
        twse_data = self._fetch_twse_data_history(code=code)
        if twse_data:
            return twse_data

        tpex_data = self._fetch_tpex_data_history(code=code)
        if tpex_data:
            return tpex_data

        raise ValueError(f'{code} {self.date_} result not found')
