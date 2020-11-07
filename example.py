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
from tw_stock_plugin import StockInfo, StockTrading, StockInstitutionalInvestors, StockTools, UpdateStock

if __name__ == '__main__':
    # init stock info object
    stock_info = StockInfo()
    # get all stocks info
    print(stock_info.get())
    # get 1101 stock info
    print(stock_info.get('110'))
    # get 1101 stock name
    print(stock_info.get('1101').name)
    # get 1101 B stock name, it will return value error because it doesn't exists
    print(stock_info.get('1101 B'))

    # check if 2020/10/10 is open date, it will return False
    print(StockTools.check_is_open_date(datetime.strptime('2020/10/10', '%Y/%m/%d').date()))
    # check if 2020/10/23 is open date, it will return True
    print(StockTools.check_is_open_date(datetime.strptime('2020/10/23', '%Y/%m/%d').date()))
    # check if 2020/10/23 is open date, it will type error because it's not type of datetime.time
    print(StockTools.check_is_open_date('2020/03/18'))

    # convert 109/10/10 to ad, it allow Y/m/d and Y-m-d format
    print(StockTools.republic_era_to_ad(date_='109/10/10'))
    # convert 2020/10/10 to republic era, it allow Y/m/d and Y-m-d format
    print(StockTools.ad_to_republic_era(date_='2020/10/10'))

    # setting target date
    date_ = datetime(2020, 10, 30).date()

    # init stock trading object with specific date
    stock_trading = StockTrading(date_=date_)

    # getting all trading data in 2020/10/30
    trading_all = stock_trading.get_all()

    # getting 2330 trading data in 2020/10/30
    trading_2330 = trading_all['2330']
    # print 2330 name
    print(trading_2330.name)
    # print 2330 code
    print(trading_2330.code)
    # print 2330 trade_value
    print(trading_2330.trade_value)
    # print 2330 closing_price
    print(trading_2330.closing_price)

    # getting monthly history trading data of 1101 in 2020/10
    trading_history_1101 = stock_trading.get_history(code=1101)
    # get only 2020/10/30 trading data
    print(trading_history_1101[date_])

    # getting monthly history trading data of 9962 in 2020/10
    trading_history_9962 = stock_trading.get_history(code=9962)
    # get only 2020/10/30 trading data
    print(trading_history_9962[date_])

    # init stock institutional investors object with specific date
    stock_institutional_investors = StockInstitutionalInvestors(date_=date_)

    # getting all institutional investors data in 2020/10/30
    institutional_investors_all = stock_institutional_investors.get_all()

    # getting 2330 institutional investors data in 2020/10/30
    institutional_investors_2330 = institutional_investors_all['2330']
    # print 2330 foreign mainland area buy
    print(institutional_investors_2330.foreign_mainland_area_buy)
    # getting 3529 institutional investors data in 2020/10/30
    institutional_investors_3529 = institutional_investors_all['3529']
    # print 3529 foreign mainland area buy
    print(institutional_investors_3529.trust_diff)
    # update newest stock info
    UpdateStock.main()
