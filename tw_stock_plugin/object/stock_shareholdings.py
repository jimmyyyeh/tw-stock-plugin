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

from datetime import datetime

from tw_stock_plugin.constant import StockShareholdings
from tw_stock_plugin.utils.schema import SchemaPattern


class StockShareholdingsObject:
    def __init__(self, date, code, index, number_of_shareholders, total_shares,
                 percentage_over_total_shares, number_of_shares=None):
        """
        :param date: 日期
        :param code: 股票代碼
        :param index: 序
        :param number_of_shares: 持股/單位數分級
        :param number_of_shareholders: 人數
        :param total_shares: 股數/單位數
        :param percentage_over_total_shares: 占集保庫存數比例 (%)
        :return:
        """
        self.date = datetime.strptime(str(date), '%Y%m%d').date()
        self.code = code
        self.index = index
        self.number_of_shares = number_of_shares or self._transfer_number_of_shares()
        self.number_of_shareholders = number_of_shareholders
        self.total_shares = total_shares
        self.percentage_over_total_shares = percentage_over_total_shares
        self._format_value()
        # self._valid_schema()

    def _transfer_number_of_shares(self):
        if self.index not in StockShareholdings.NUMBER_OF_SHARES_DICT:
            return None
        return StockShareholdings.NUMBER_OF_SHARES_DICT[self.index]

    def _format_value(self):
        integer_keys = {'index', 'number_of_shareholders', 'total_shares'}
        float_keys = {'percentage_over_total_shares'}
        for key in integer_keys:
            value = getattr(self, key)
            setattr(self, key, int(value))

        for key in float_keys:
            value = getattr(self, key)
            setattr(self, key, float(value))

    def _valid_schema(self):
        SchemaPattern.StockShareholdingsSchema.validate(self.__dict__)
