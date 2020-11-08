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


class StockInfoObject:
    def __init__(self, code, name, ISIN_code, listed_date, category, industry, CFI_code, type):
        """
        :param code: 股票代碼
        :param name: 股票名稱
        :param ISIN_code: 國際證券辨識號碼(ISIN Code)
        :param listed_date: 上市/上櫃/興櫃 日
        :param category: 市場別
        :param industry: 產業別
        :param CFI_code: CFICode
        :param type: 證券類別
        """
        self.code = code
        self.name = name
        self.ISIN_code = ISIN_code
        self.listed_date = listed_date
        self.category = category
        self.industry = industry
        self.CFI_code = CFI_code
        self.type = type
