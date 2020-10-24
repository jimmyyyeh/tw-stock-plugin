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

from tw_stock_plugin.core._stock_info import StockInfo


class StockPlugin:
    StockInfo = StockInfo


if __name__ == '__main__':
    # init stock info object
    stock_info = StockPlugin.StockInfo()

    # get all stocks info
    print(stock_info.get())

    # get 1101 stock info
    print(stock_info.get('1101'))

    # get 1101 stock name
    print(stock_info.get('1101').name)

    # get 1101 B stock name, it will return value error because it doesn't exists
    print(stock_info.get('1101 B'))
