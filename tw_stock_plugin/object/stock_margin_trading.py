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
        self.balance_of_previous_day_cash = cash_balance_of_previous_day
        self.balance_of_the_day_cash = cash_balance_of_the_day
        self.quota_cash = cash_quota
        self.short_covering = short_covering
        self.short_sale = short_sale
        self.stock_redemption = stock_redemption
        self.balance_of_previous_day_stock = stock_balance_of_previous_day
        self.balance_of_the_day_stock_cash = stock_balance_of_the_day
        self.quota_stock = stock_quota
        self.offset = offset
        self.note = note
        self._format_value()

    def _format_value(self):
        for key, value in self.__dict__.items():
            if value and ',' in value:
                setattr(self, key, float(value.replace(',', '')))
            elif key in {'code', 'name', 'note'}:
                setattr(self, key, value.strip())
            else:
                setattr(self, key, float(value.strip()))


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
        self.balance_of_previous_day_cash = cash_balance_of_previous_day
        self.margin_purchase = margin_purchase
        self.margin_sells = margin_sells
        self.cash_redemption = cash_redemption
        self.balance_of_the_day_cash = cash_balance_of_the_day
        self.cash_belong_to_securities_finance = cash_belong_to_securities_finance
        self.cash_utilization_rate = cash_utilization_rate
        self.quota_cash = cash_quota
        self.balance_of_previous_day_stock = stock_balance_of_previous_day
        self.short_covering = short_covering
        self.short_sale = short_sale
        self.stock_redemption = stock_redemption
        self.balance_of_the_day_stock_cash = stock_balance_of_the_day
        self.stock_belong_to_securities_finance = stock_belong_to_securities_finance
        self.stock_utilization_rate = stock_utilization_rate
        self.quota_stock = stock_quota
        self.offset = offset
        self.note = note
        self._format_value()

    def _format_value(self):
        for key, value in self.__dict__.items():
            if value and ',' in value:
                setattr(self, key, float(value.replace(',', '')))
            elif key in {'code', 'name', 'note'}:
                setattr(self, key, value.strip())
            else:
                setattr(self, key, float(value.strip()))
