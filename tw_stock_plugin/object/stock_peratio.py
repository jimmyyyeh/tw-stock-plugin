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
from tw_stock_plugin.utils.schema import SchemaPattern


class StockPERatioObject:
    def __init__(self, yield_ratio, pbr, per, code=None, name=None, dividend_year=None, date_=None,
                 dividend_per_share=None,
                 fiscal_year_quarter=None):
        """
        :param code: 股票代碼
        :param name: 股票名稱
        :param date_: 資料日期
        :param per: 本益比
        :param dividend_per_share: 每股股利
        :param dividend_year: 股利年度
        :param yield_ratio: 殖利率(%)
        :param pbr: 股價淨值比
        :param fiscal_year_quarter: 財報年/季
        """
        self.code = code
        self.name = name
        self.date = date_
        self.per = per
        self.dividend_per_share = dividend_per_share
        self.dividend_year = dividend_year
        self.yield_ratio = yield_ratio
        self.pbr = pbr
        self.fiscal_year_quarter = fiscal_year_quarter
        self._format_value()
        # self._valid_schema()

    def _format_value(self):
        integer_keys = {'dividend_year'}
        float_keys = {'per', 'dividend_per_share', 'yield_ratio', 'pbr'}
        for key, value in self.__dict__.items():
            value = value.strip() if isinstance(value, str) else value
            if value is None:
                continue
            elif key in integer_keys:
                value = int(value)
            elif key in float_keys:
                if value in {'N/A', '-', ''}:
                    value = None
                elif isinstance(value, str) and ',' in value:
                    value = float(value.replace(',', ''))
                else:
                    value = float(value)
            setattr(self, key, value)

    def _valid_schema(self):
        SchemaPattern.StockPERatioSchema.validate(self.__dict__)
