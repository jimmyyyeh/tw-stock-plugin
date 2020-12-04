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


class InstitutionalInvestorsObject:
    def __init__(self, code, name, foreign_mainland_area_buy, foreign_mainland_area_sell, foreign_mainland_area_diff,
                 foreign_buy, foreign_sell, foreign_diff, trust_buy, trust_sell, trust_diff, proprietary_dealers_buy,
                 proprietary_dealers_sell, proprietary_dealers_diff, hedge_dealers_buy, hedge_dealers_sell,
                 hedge_dealers_diff, total_diff):
        """
        :param code: 股票代碼
        :param name: 股票名稱
        :param foreign_mainland_area_buy: 外陸資買進股數(不含外資自營商)
        :param foreign_mainland_area_sell: 外陸資賣出股數(不含外資自營商)
        :param foreign_mainland_area_diff: 外陸資買賣超股數(不含外資自營商)
        :param foreign_buy: 外資自營商買進股數
        :param foreign_sell: 外資自營商賣出股數
        :param foreign_diff: 外資自營商買賣超股數
        :param trust_buy: 投信買進股數
        :param trust_sell: 投信賣出股數
        :param trust_diff: 投信買賣超股數
        :param proprietary_dealers_buy: 自營商買進股數(自行買賣)
        :param proprietary_dealers_sell: 自營商賣出股數(自行買賣)
        :param proprietary_dealers_diff: 自營商買賣超股數(自行買賣)
        :param hedge_dealers_buy: 自營商買進股數(避險)
        :param hedge_dealers_sell: 自營商賣出股數(避險)
        :param hedge_dealers_diff: 自營商買賣超股數(避險)
        :param total_diff: 三大法人買賣超股數
        """
        self.code = code
        self.name = name
        self.foreign_mainland_area_buy = foreign_mainland_area_buy
        self.foreign_mainland_area_sell = foreign_mainland_area_sell
        self.foreign_mainland_area_diff = foreign_mainland_area_diff
        self.foreign_buy = foreign_buy
        self.foreign_sell = foreign_sell
        self.foreign_diff = foreign_diff
        self.trust_buy = trust_buy
        self.trust_sell = trust_sell
        self.trust_diff = trust_diff
        self.proprietary_dealers_buy = proprietary_dealers_buy
        self.proprietary_dealers_sell = proprietary_dealers_sell
        self.proprietary_dealers_diff = proprietary_dealers_diff
        self.hedge_dealers_buy = hedge_dealers_buy
        self.hedge_dealers_sell = hedge_dealers_sell
        self.hedge_dealers_diff = hedge_dealers_diff
        self.total_diff = total_diff
        self._format_value()
        # self._valid_schema()

    def _format_value(self):
        floats_keys = {'foreign_mainland_area_buy', 'foreign_mainland_area_sell', 'foreign_mainland_area_diff',
                       'foreign_buy', 'foreign_sell', 'foreign_diff', 'trust_buy', 'trust_sell', 'trust_diff',
                       'proprietary_dealers_buy', 'proprietary_dealers_sell', 'proprietary_dealers_diff',
                       'hedge_dealers_buy', 'hedge_dealers_sell', 'hedge_dealers_diff', 'total_diff'}
        for key, value in self.__dict__.items():
            value = value.strip() if isinstance(value, str) else value
            if value is None:
                continue
            elif key in floats_keys:
                if isinstance(value, str) and ',' in value:
                    value = float(value.replace(',', ''))
                elif value == '':
                    value = None
                else:
                    value = float(value)
            setattr(self, key, value)

    def _valid_schema(self):
        SchemaPattern.StockInstitutionalInvestorsSchema.validate(self.__dict__)
