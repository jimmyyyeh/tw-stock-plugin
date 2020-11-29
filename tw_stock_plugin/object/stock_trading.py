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
from tw_stock_plugin.regex_pattern import TradingPattern
from tw_stock_plugin.utils.schema import SchemaPattern


class TwseTradingObject:
    def __init__(self, trading_volume, transaction, trade_value, opening_price, highest_price, lowest_price,
                 closing_price, change, code=None, name=None, different=None, last_best_bid_price=None,
                 last_best_bid_volume=None, last_best_ask_price=None, last_best_ask_volume=None,
                 price_earning_rate=None):

        """
        :param code: 股票代碼
        :param name: 股票名稱
        :param trading_volume: 成交股數
        :param transaction: 成交筆數
        :param trade_value: 成交金額
        :param opening_price: 開盤價
        :param highest_price: 最高價
        :param lowest_price: 最低價
        :param closing_price: 收盤價
        :param different: 漲跌(+/-)
        :param change: 漲跌價差
        :param last_best_bid_price: 最後揭示買價
        :param last_best_bid_volume: 最後揭示賣價
        :param last_best_ask_price: 最後揭示買量
        :param last_best_ask_volume: 最後揭示買量
        :param price_earning_rate: 本益比
        """
        self.code = code
        self.name = name
        self.trading_volume = trading_volume
        self.transaction = transaction
        self.trade_value = trade_value
        self.opening_price = opening_price
        self.highest_price = highest_price
        self.lowest_price = lowest_price
        self.closing_price = closing_price
        self._different = different
        self.change = change
        self.last_best_bid_price = last_best_bid_price
        self.last_best_bid_volume = last_best_bid_volume
        self.last_best_ask_price = last_best_ask_price
        self.last_best_ask_volume = last_best_ask_volume
        self.price_earning_rate = price_earning_rate
        self._format_value()
        # self._valid_schema()

    def _format_value(self):
        # 漲跌可能為 +-x, x為不比價
        if self._different and TradingPattern.DIFFERENT_PATTERN.search(self._different):
            self._different = TradingPattern.DIFFERENT_PATTERN.search(self._different).group()
            if self._different.startswith('X'):
                self.change = None
            else:
                self.change = f'{self._different}{self.change}' if self._different else self.change

        float_keys = {'trading_volume', 'transaction', 'trade_value', 'opening_price', 'highest_price',
                      'lowest_price', 'closing_price', 'last_best_bid_price', 'last_best_bid_price', 'change',
                      'last_best_bid_volume', 'last_best_ask_price', 'last_best_ask_volume', 'price_earning_rate'}

        for key, value in self.__dict__.items():
            value = value.strip() if isinstance(value, str) else value
            if value is None:
                continue
            elif key in float_keys and not set(value) == {'-'} and value not in {'除權', '除息', '除權息'}:
                if isinstance(value, str) and ',' in value:
                    value = float(value.replace(',', ''))
                elif value == '':
                    value = None
                else:
                    value = float(value)
            elif set(value) == {'-'}:
                value = None
            setattr(self, key, value)

    def _valid_schema(self):
        SchemaPattern.TwseStockTradingSchema.validate(self.__dict__)


class TpexTradingObject:
    def __init__(self, closing_price, change, opening_price, highest_price, lowest_price, trading_volume, trade_value,
                 transaction, code=None, name=None, last_best_bid_price=None, last_best_ask_price=None,
                 last_best_bid_volume=None, last_best_ask_volume=None, issued_shares=None, next_limit_up=None,
                 next_limit_down=None):
        """
        :param code: 股票代碼
        :param name: 股票名稱
        :param closing_price: 收盤價
        :param change: 漲跌價差
        :param opening_price: 開盤價
        :param highest_price: 最高價
        :param lowest_price: 最低價
        :param trading_volume: 成交股數
        :param trade_value: 成交金額
        :param transaction: 成交筆數
        :param last_best_bid_price: 最後揭示買價
        :param last_best_ask_price: 最後揭示買量
        :param last_best_bid_volume: 最後揭示賣價
        :param last_best_ask_volume: 最後揭示買量
        :param issued_shares: 發行股數
        :param next_limit_up: 次日漲停價
        :param next_limit_down: 次日跌停價
        """
        self.code = code
        self.name = name
        self.closing_price = closing_price
        self.change = change
        self.opening_price = opening_price
        self.highest_price = highest_price
        self.lowest_price = lowest_price
        self.trading_volume = trading_volume
        self.trade_value = trade_value
        self.transaction = transaction
        self.last_best_bid_price = last_best_bid_price
        self.last_best_ask_price = last_best_ask_price
        self.last_best_bid_volume = last_best_bid_volume
        self.last_best_ask_volume = last_best_ask_volume
        self.issued_shares = issued_shares
        self.next_limit_up = next_limit_up
        self.next_limit_down = next_limit_down
        self._format_value()
        # self._valid_schema()

    def _format_value(self):
        float_keys = {'closing_price', 'change', 'opening_price', 'highest_price', 'lowest_price', 'trading_volume',
                      'trade_value', 'transaction', 'last_best_bid_price', 'last_best_ask_price', 'change',
                      'last_best_bid_volume', 'last_best_ask_volume', 'issued_shares', 'next_limit_up',
                      'next_limit_down'}

        for key, value in self.__dict__.items():
            value = value.strip() if isinstance(value, str) else value
            if value is None:
                continue
            elif key in float_keys and not set(value) == {'-'} and value not in {'除權', '除息', '除權息'}:
                if isinstance(value, str) and ',' in value:
                    value = float(value.replace(',', ''))
                elif value == '':
                    value = None
                else:
                    value = float(value)
            elif set(value) == {'-'}:
                value = None
            setattr(self, key, value)

        if self.code and self.name:
            self.last_best_bid_volume = self.last_best_bid_volume * 1000 if self.last_best_bid_volume else None
            self.last_best_ask_volume = self.last_best_ask_volume * 1000 if self.last_best_ask_volume else None
        else:
            self.trading_volume = self.trading_volume * 1000 if self.trading_volume else None
            self.trade_value = self.trade_value * 1000 if self.trade_value else None

    def _valid_schema(self):
        SchemaPattern.TpexStockTradingSchema.validate(self.__dict__)
