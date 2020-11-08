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
from tw_stock_plugin.object.stock_margin_trading import TwseMarginTradingObject, TpexMarginTradingObject
from tw_stock_plugin.constant import Domain
from tw_stock_plugin.utils.response_handler import ResponseHandler


class StockMarginTrading:
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
        fetch all margin trading data in specific date from twse website
        :return:
        """
        margin_trading_dict = dict()
        url = f'{Domain.TAIWAN_STOCK_EXCHANGE_CORPORATION}/exchangeReport/MI_MARGN'
        query_date = self.date_.strftime('%Y%m%d')
        params = {
            'response': 'json',
            'date': query_date,
            'selectType': 'ALL'
        }
        response = ResponseHandler.get(url=url, params=params)
        if not response:
            return None
        json_data = response.json()
        stats = json_data['stat']
        if not stats == 'OK':
            return None
        data_list = json_data['data']
        columns = ['code', 'name', 'margin_purchase', 'margin_sells', 'cash_redemption', 'cash_balance_of_previous_day',
                   'cash_balance_of_the_day', 'cash_quota', 'short_covering', 'short_sale', 'stock_redemption',
                   'stock_balance_of_previous_day', 'stock_balance_of_the_day', 'stock_quota', 'offset', 'note']
        for data in data_list:
            stock_margin_trading = TwseMarginTradingObject(**dict(zip(columns, data)))
            margin_trading_dict[stock_margin_trading.code] = stock_margin_trading
        return margin_trading_dict

    def _fetch_tpex_data_all(self):
        """
        fetch all margin trading data in specific date from tpex website
        :return:
        """
        margin_trading_dict = dict()
        url = f'{Domain.TAIPEI_EXCHANGE}/web/stock/margin_trading/margin_balance/margin_bal_result.php'
        query_date = StockTools.ad_to_republic_era(date_=self.date_).replace('-', '/'),
        params = {
            'l': 'zh-tw',
            'o': 'json',
            'd': query_date
        }
        response = ResponseHandler.get(url=url, params=params)
        if not response:
            return None
        json_data = response.json()
        data_list = json_data['aaData']
        if not data_list:
            return None
        columns = ['code', 'name', 'cash_balance_of_previous_day', 'margin_purchase', 'margin_sells', 'cash_redemption',
                   'cash_balance_of_the_day', 'cash_belong_to_securities_finance', 'cash_utilization_rate',
                   'cash_quota', 'stock_balance_of_previous_day', 'short_covering', 'short_sale', 'stock_redemption',
                   'stock_balance_of_the_day', 'stock_belong_to_securities_finance', 'stock_utilization_rate',
                   'stock_quota', 'offset', 'note']
        for data in data_list:
            stock_margin_trading = TpexMarginTradingObject(**dict(zip(columns, data)))
            margin_trading_dict[stock_margin_trading.code] = stock_margin_trading
        return margin_trading_dict

    def get_all(self):
        """
        return all margin trading data
        :return:
        """
        margin_trading_dict = dict()
        twse_data = self._fetch_twse_data_all()
        tpex_data = self._fetch_tpex_data_all()
        if twse_data:
            margin_trading_dict.update(twse_data)
        if tpex_data:
            margin_trading_dict.update(tpex_data)
        return margin_trading_dict
