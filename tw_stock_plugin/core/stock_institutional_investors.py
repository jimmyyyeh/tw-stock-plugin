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
from tw_stock_plugin.object.stock_institutional_investors import InstitutionalInvestorsObject
from tw_stock_plugin.constant import Domain
from tw_stock_plugin.utils.response_handler import ResponseHandler


class StockInstitutionalInvestors:
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
        fetch all institutional investors data in specific date from twse website
        :return:
        """
        institutional_investors_dict = dict()
        url = f'{Domain.TAIWAN_STOCK_EXCHANGE_CORPORATION}/fund/T86'
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
        columns = ['code', 'name', 'foreign_mainland_area_buy', 'foreign_mainland_area_sell',
                   'foreign_mainland_area_diff', 'foreign_buy', 'foreign_sell', 'foreign_diff', 'trust_buy',
                   'trust_sell', 'trust_diff', 'proprietary_dealers_buy', 'proprietary_dealers_sell',
                   'proprietary_dealers_diff', 'hedge_dealers_buy', 'hedge_dealers_sell', 'hedge_dealers_diff',
                   'total_diff']
        removed_indices = {11}
        for data in data_list:
            data = [value for index, value in enumerate(data) if index not in removed_indices]
            if len(columns) != len(data):
                print(f'{data[0]} MISSING INSTITUTIONAL INVESTORS MISSING')
                continue
            stock_institutional_investors = InstitutionalInvestorsObject(**dict(zip(columns, data)))
            institutional_investors_dict[stock_institutional_investors.code] = stock_institutional_investors
        return institutional_investors_dict

    def _fetch_tpex_data_all(self):
        """
        fetch all institutional investors data in specific date from tpex website
        :return:
        """
        institutional_investors_dict = dict()
        url = f'{Domain.TAIPEI_EXCHANGE}/web/stock/3insti/daily_trade/3itrade_hedge_result.php'
        query_date = StockTools.ad_to_republic_era(date_=self.date_).replace('-', '/'),
        params = {
            'l': 'zh-tw',
            'd': query_date,
            'se': 'EW',
            't': 'D'
        }
        response = ResponseHandler.get(url=url, params=params)
        if not response:
            return None
        json_data = response.json()
        data_list = json_data['aaData']
        if not data_list:
            return None
        columns = ['code', 'name', 'foreign_mainland_area_buy', 'foreign_mainland_area_sell',
                   'foreign_mainland_area_diff', 'foreign_buy', 'foreign_sell', 'foreign_diff', 'trust_buy',
                   'trust_sell', 'trust_diff', 'proprietary_dealers_buy', 'proprietary_dealers_sell',
                   'proprietary_dealers_diff', 'hedge_dealers_buy', 'hedge_dealers_sell', 'hedge_dealers_diff',
                   'total_diff']
        removed_indices = {8, 9, 10, 20, 21, 22, 24}
        for data in data_list:
            data = [value for index, value in enumerate(data) if index not in removed_indices]
            if len(columns) != len(data):
                print(f'{data[0]} MISSING INSTITUTIONAL INVESTORS MISSING')
                continue
            stock_institutional_investors = InstitutionalInvestorsObject(**dict(zip(columns, data)))
            institutional_investors_dict[stock_institutional_investors.code] = stock_institutional_investors
        return institutional_investors_dict

    def get_all(self):
        """
        return all institutional investors data
        :return:
        """
        institutional_investors_dict = dict()
        twse_data = self._fetch_twse_data_all()
        tpex_data = self._fetch_tpex_data_all()
        if twse_data:
            institutional_investors_dict.update(twse_data)
        if tpex_data:
            institutional_investors_dict.update(tpex_data)
        return institutional_investors_dict
