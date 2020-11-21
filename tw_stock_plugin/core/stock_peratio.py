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

from datetime import date, datetime

from tw_stock_plugin.core.stock_tools import StockTools
from tw_stock_plugin.constant import Domain
from tw_stock_plugin.object.stock_peratio import StockPERatioObject
from tw_stock_plugin.utils.response_handler import ResponseHandler
from tw_stock_plugin.regex_pattern import PERatioPattern


class StockPERatio:
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

    @staticmethod
    def _translate_date(date_):
        """
        translate date from chinese to correct format
        :param date_:
        :return:
        """
        year, month, day = PERatioPattern.CHINESE_DATE_PATTERN.search(date_).groups()
        return f'{year}/{month}/{day}'

    def _fetch_twse_data_all(self):
        """
        fetch all p/e ratio, dividend yield and p/b ratio data in specific date from twse website
        :return:
        """
        p_e_ratio_dict = dict()
        url = f'{Domain.TAIWAN_STOCK_EXCHANGE_CORPORATION}/exchangeReport/BWIBBU_d'
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
        columns = ['code', 'name', 'yield_ratio', 'dividend_year', 'per', 'pbr', 'fiscal_year_quarter']
        for data in data_list:
            p_e_ratio = StockPERatioObject(**dict(zip(columns, data)))
            p_e_ratio_dict[p_e_ratio.code] = p_e_ratio
        return p_e_ratio_dict

    def _fetch_tpex_data_all(self):
        """
        fetch all p/e ratio, dividend yield and p/b ratio data in specific date from tpex website
        :return:
        """
        p_e_ratio_dict = dict()
        url = f'{Domain.TAIPEI_EXCHANGE}/web/stock/aftertrading/peratio_analysis/pera_result.php'
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
        columns = ['code', 'name', 'per', 'dividend_per_share', 'dividend_year', 'yield_ratio', 'pbr']
        for data in data_list:
            p_e_ratio = StockPERatioObject(**dict(zip(columns, data)))
            p_e_ratio_dict[p_e_ratio.code] = p_e_ratio
        return p_e_ratio_dict

    def get_all(self):
        """
        return all p/e ratio, dividend yield and p/b ratio data
        :return:
        """
        p_e_ratio_dict = dict()
        twse_data = self._fetch_twse_data_all()
        tpex_data = self._fetch_tpex_data_all()
        if twse_data:
            p_e_ratio_dict.update(twse_data)
        if tpex_data:
            p_e_ratio_dict.update(tpex_data)
        return p_e_ratio_dict

    def _fetch_twse_data_history(self, code):
        """
        get specific stock monthly p/e ratio, dividend yield and p/b ratio data from twse website
        :param code:
        :return:
        """
        p_e_ratio_dict = dict()
        url = f'{Domain.TAIWAN_STOCK_EXCHANGE_CORPORATION}/exchangeReport/BWIBBU'
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
        columns = ['yield_ratio', 'dividend_year', 'per', 'pbr', 'fiscal_year_quarter']

        for data in data_list:
            date_ = self._translate_date(data[0])
            date_ = StockTools.republic_era_to_ad(date_)
            date_ = datetime.strptime(date_, '%Y/%m/%d').date()
            p_e_ratio = StockPERatioObject(**(dict(zip(columns, data[1:]))))
            for attr in p_e_ratio.__dict__.copy():
                if attr not in columns:
                    delattr(p_e_ratio, attr)
            p_e_ratio_dict[date_] = p_e_ratio
        return p_e_ratio_dict

    def _fetch_tpex_data_history(self, code):
        """
        get specific stock monthly p/e ratio, dividend yield and p/b ratio data from tpex website
        :param code:
        :return:
        """
        p_e_ratio_dict = dict()
        url = f'{Domain.TAIPEI_EXCHANGE}/web/stock/aftertrading/peratio_stk/pera_result.php?'
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
        columns = ['per', 'yield_ratio', 'dividend_year', 'pbr']
        for data in data_list:
            date_ = StockTools.republic_era_to_ad(data[0])
            date_ = datetime.strptime(date_, '%Y/%m/%d').date()
            p_e_ratio = StockPERatioObject(**(dict(zip(columns, data[1:]))))
            for attr in p_e_ratio.__dict__.copy():
                if attr not in columns:
                    delattr(p_e_ratio, attr)
            p_e_ratio_dict[date_] = p_e_ratio
        return p_e_ratio_dict

    def get_history(self, code):
        """
        return monthly p/e ratio, dividend yield and p/b ratio data with specific stock code
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
