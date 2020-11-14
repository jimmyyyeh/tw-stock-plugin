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

import pandas as pd
from time import sleep
from datetime import date, datetime

from tw_stock_plugin.object.stock_shareholdings import StockShareholdingsObject
from tw_stock_plugin.utils.response_handler import ResponseHandler
from tw_stock_plugin.constant import Domain


class StockShareholdings:
    def __init__(self):
        pass

    @staticmethod
    def _valid_date(date_, date_list):
        """
        check date format and if date in valid date list
        """
        if not isinstance(date_, date):
            raise TypeError('input date must be type of datetime.date')
        elif date_ not in date_list:
            raise ValueError('input date no available')
        else:
            return date_.strftime('%Y%m%d')

    @staticmethod
    def _get_available_date_list():
        url = f'{Domain.TDCC}/smWeb/QryStockAjax.do'
        headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) '
                                 'AppleWebKit/537.36 (KHTML, liek Gecko) Chrome/34.0.1847.131 Safari/537.36'}
        payload = {
            'REQ_OPR': 'qrySelScaDates'
        }
        while True:
            response = ResponseHandler.post(url=url, payload=payload, headers=headers)
            date_list = response.json()
            date_list = [datetime.strptime(date_, '%Y%m%d').date() for date_ in date_list]
            if date_list:
                return date_list
            print('fetching date list error, retry after 3 seconds...')
            sleep(3)

    @staticmethod
    def _fetch_single_data(code, date_):
        url = f'{Domain.TDCC}/smWeb/QryStockAjax.do'
        headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) '
                                 'AppleWebKit/537.36 (KHTML, liek Gecko) Chrome/34.0.1847.131 Safari/537.36'}
        payload = {
            'scaDates': date_,
            'scaDate': date_,
            'SqlMethod': 'StockNo',
            'StockNo': code,
            'radioStockNo': code,
            'StockName': '',
            'REQ_OPR': 'SELECT',
            'clkStockNo': code,
            'clkStockName': '',
        }
        while True:
            response = ResponseHandler.post(url=url, payload=payload, headers=headers)
            if '無此資料' not in response:
                return response
            print('fetching data error, retry after 3 seconds...')
            sleep(3)

    def get_by_query(self, code, date_):
        """
        fetch shareholdings data with specific code and date
        :param code:
        :param date_:
        :return:
        """
        date_list = self._get_available_date_list()
        date_ = self._valid_date(date_=date_, date_list=date_list)

        shareholdings_dict = dict()
        response = self._fetch_single_data(code=code, date_=date_)
        df = pd.read_html(response.text)[0]
        df = df.dropna()
        columns = ['date', 'code', 'index', 'number_of_shares', 'number_of_shareholders', 'total_shares',
                   'percentage_over_total_shares']
        df = df.iloc[1:]
        for data in df.values.tolist():
            data = [date_, code] + data
            stock_shareholdings = StockShareholdingsObject(**(dict(zip(columns, data))))
            if not stock_shareholdings.index:
                continue
            shareholdings_dict[stock_shareholdings.index] = stock_shareholdings
        return shareholdings_dict

    @staticmethod
    def get_newest():
        """
        fetch newest shareholdings data from official website
        :return:
        """
        shareholdings_dict = dict()
        url = f'{Domain.SMART_TDCC}/opendata/getOD.ashx'
        headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) '
                                 'AppleWebKit/537.36 (KHTML, liek Gecko) Chrome/34.0.1847.131 Safari/537.36'}
        params = {
            'id': '1-5'
        }
        response = ResponseHandler.get(url=url, params=params, headers=headers)
        df = pd.read_csv(response.url)
        columns = ['date', 'code', 'index', 'number_of_shareholders', 'total_shares',
                   'percentage_over_total_shares']
        for data in df.values.tolist():
            stock_shareholdings = StockShareholdingsObject(**(dict(zip(columns, data))))
            if not stock_shareholdings.number_of_shares:
                continue
            if stock_shareholdings.code not in shareholdings_dict:
                shareholdings_dict[stock_shareholdings.code] = dict()
            shareholdings_dict[stock_shareholdings.code].update({stock_shareholdings.index: stock_shareholdings})
        return shareholdings_dict
