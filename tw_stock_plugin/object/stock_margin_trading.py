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
from tw_stock_plugin.regex_pattern import MarginTradingPattern
from tw_stock_plugin.utils.schema import SchemaPattern


class TwseMarginTradingObject:
    def __init__(self, code, name, margin_purchase, margin_sells, cash_redemption, cash_balance_of_previous_day,
                 cash_balance_of_the_day, cash_quota, short_covering, short_sale, stock_redemption,
                 stock_balance_of_previous_day, stock_balance_of_the_day, stock_quota, offset, note):
        """
        :param code: 股票代碼
        :param name: 股票名稱
        :param margin_purchase: 融資買進
        :param margin_sells: 融資賣出
        :param cash_redemption: 現金償還
        :param cash_balance_of_previous_day: 前日餘額
        :param cash_balance_of_the_day: 今日餘額
        :param cash_quota: 限額
        :param short_covering: 融券買進
        :param short_sale: 融券賣出
        :param stock_redemption: 現金償還
        :param stock_balance_of_previous_day: 前日餘額
        :param stock_balance_of_the_day: 今日餘額
        :param stock_quota: 限額
        :param offset: 資券互抵
        :param note: 備註
        """
        self.code = code
        self.name = name
        self.margin_purchase = margin_purchase
        self.margin_sells = margin_sells
        self.cash_redemption = cash_redemption
        self.cash_balance_of_previous_day = cash_balance_of_previous_day
        self.cash_balance_of_the_day = cash_balance_of_the_day
        self.cash_quota = cash_quota
        self.short_covering = short_covering
        self.short_sale = short_sale
        self.stock_redemption = stock_redemption
        self.stock_balance_of_previous_day = stock_balance_of_previous_day
        self.stock_balance_of_the_day = stock_balance_of_the_day
        self.stock_quota = stock_quota
        self.offset = offset
        self.note = note
        self._format_value()
        # self._valid_schema()

    def _format_value(self):
        float_keys = {'margin_purchase', 'margin_sells', 'cash_redemption', 'cash_balance_of_previous_day',
                      'cash_balance_of_the_day', 'cash_quota', 'short_covering', 'short_sale', 'stock_redemption',
                      'stock_balance_of_previous_day', 'stock_balance_of_the_day', 'stock_quota', 'offset'}
        for key, value in self.__dict__.items():
            value = value.strip() if isinstance(value, str) else value
            if value is None:
                continue
            elif key in float_keys:
                if isinstance(value, str) and ',' in value:
                    value = float(value.replace(',', ''))
                elif value == '':
                    value = None
                else:
                    value = float(value)
            elif key in {'note'}:
                if MarginTradingPattern.NOTE_STRIP_PATTERN.search(value):
                    value = MarginTradingPattern.NOTE_STRIP_PATTERN.sub(',', value)
                elif value == '':
                    value = None
            setattr(self, key, value)

    def _valid_schema(self):
        SchemaPattern.TwseStockMarginTradingSchema.validate(self.__dict__)


class TpexMarginTradingObject:
    def __init__(self, code, name, cash_balance_of_previous_day, margin_purchase, margin_sells, cash_redemption,
                 cash_balance_of_the_day, cash_belong_to_securities_finance, cash_utilization_rate, cash_quota,
                 stock_balance_of_previous_day, short_covering, short_sale, stock_redemption, stock_balance_of_the_day,
                 stock_belong_to_securities_finance, stock_utilization_rate, stock_quota, offset, note):
        """
        :param code: 股票代碼
        :param name: 股票名稱
        :param cash_balance_of_previous_day: 前日餘額
        :param margin_purchase: 融資買進
        :param margin_sells: 融資賣出
        :param cash_redemption: 現金償還
        :param cash_balance_of_the_day: 今日餘額
        :param cash_belong_to_securities_finance: 資屬證金
        :param cash_utilization_rate(%): 資使用率(%)
        :param cash_quota: 限額
        :param stock_balance_of_previous_day: 前日餘額
        :param short_covering: 融券買進
        :param short_sale: 融券賣出
        :param stock_redemption: 現金償還
        :param stock_balance_of_the_day: 今日餘額
        :param stock_belong_to_securities_finance: 券屬證金
        :param stock_utilization_rate(%): 券使用率(%)
        :param stock_quota: 限額
        :param offset: 資券互抵
        :param note: 備註
        """
        self.code = code
        self.name = name
        self.cash_balance_of_previous_day = cash_balance_of_previous_day
        self.margin_purchase = margin_purchase
        self.margin_sells = margin_sells
        self.cash_redemption = cash_redemption
        self.cash_balance_of_the_day = cash_balance_of_the_day
        self.cash_belong_to_securities_finance = cash_belong_to_securities_finance
        self.cash_utilization_rate = cash_utilization_rate
        self.cash_quota = cash_quota
        self.stock_balance_of_previous_day = stock_balance_of_previous_day
        self.short_covering = short_covering
        self.short_sale = short_sale
        self.stock_redemption = stock_redemption
        self.stock_balance_of_the_day = stock_balance_of_the_day
        self.stock_belong_to_securities_finance = stock_belong_to_securities_finance
        self.stock_utilization_rate = stock_utilization_rate
        self.stock_quota = stock_quota
        self.offset = offset
        self.note = note
        self._format_value()
        # self._valid_schema()

    def _format_value(self):
        float_keys = {'cash_balance_of_previous_day', 'margin_purchase', 'margin_sells', 'cash_redemption',
                      'cash_balance_of_the_day', 'cash_belong_to_securities_finance', 'cash_utilization_rate',
                      'cash_quota', 'stock_balance_of_previous_day', 'short_covering', 'short_sale',
                      'stock_redemption', 'stock_balance_of_the_day', 'stock_belong_to_securities_finance',
                      'stock_utilization_rate', 'stock_quota', 'offset'}
        for key, value in self.__dict__.items():
            value = value.strip() if isinstance(value, str) else value
            if value is None:
                continue
            elif key in float_keys:
                if isinstance(value, str) and ',' in value:
                    value = float(value.replace(',', ''))
                elif value == '':
                    value = None
                else:
                    value = float(value)
            elif key in {'note'}:
                if MarginTradingPattern.NOTE_STRIP_PATTERN.search(value):
                    value = MarginTradingPattern.NOTE_STRIP_PATTERN.sub(',', value)
                elif value == '':
                    value = None
            setattr(self, key, value)

    def _valid_schema(self):
        SchemaPattern.TpexStockMarginTradingSchema.validate(self.__dict__)
