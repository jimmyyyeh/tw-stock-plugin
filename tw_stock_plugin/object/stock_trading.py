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


class TwseTradingObject:
    def __init__(self, code, name, trading_volume, transaction, trade_value, opening_price, highest_price, lowest_price,
                 closing_price, different, change, last_best_bid_price, last_best_bid_volume, last_best_ask_price,
                 last_best_ask_volume, price_earning_rate):
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
        :param different: 漲跌幅
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
        self.different = different
        self.change = change
        self.last_best_bid_price = last_best_bid_price
        self.last_best_bid_volume = last_best_bid_volume
        self.last_best_ask_price = last_best_ask_price
        self.last_best_ask_volume = last_best_ask_volume
        self.price_earning_rate = price_earning_rate
        self._format_value()

    def _format_value(self):
        self.different = TradingPattern.DIFFERENT_PATTERN.search(self.different).group() \
            if TradingPattern.DIFFERENT_PATTERN.search(self.different) else None
        for key, value in self.__dict__.items():
            if value == '--':
                setattr(self, key, None)
            if value and ',' in value:
                setattr(self, key, float(value.replace(',', '')))


class TpexTradingObject:
    def __init__(self, code, name, closing_price, change, opening_price, highest_price, lowest_price, trading_volume,
                 trade_value, transaction, last_best_bid_price, last_best_ask_price, last_best_bid_volume,
                 last_best_ask_volume, issued_shares, next_limit_up, next_limit_down_next):
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
        :param next_limit_down_next: 次日跌停價
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
        self.next_limit_down_next = next_limit_down_next
        self._format_value()

    def _format_value(self):
        for key, value in self.__dict__.items():
            if value == '----':
                setattr(self, key, None)
            if value and ',' in value:
                setattr(self, key, float(value.replace(',', '')))

        self.last_best_bid_volume = self.last_best_bid_volume * 1000 if self.last_best_bid_volume else None
        self.last_best_ask_volume = self.last_best_ask_volume * 1000 if self.last_best_ask_volume else None
