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
from tw_stock_plugin import StockInfo, StockTrading, StockInstitutionalInvestors, StockMarginTrading, \
    StockShareholdings, StockTools, UpdateStock

if __name__ == '__main__':
    """ basic info """
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

    """ daily trading """
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

    """ institutional investors """
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

    """ margin trading """
    # init stock margin trading object with specific date
    stock_margin_trading = StockMarginTrading(date_=date_)
    # getting all margin trading data in 2020/10/30
    margin_trading_all = stock_margin_trading.get_all()
    # getting 2330 margin trading data in 2020/10/30
    margin_trading_2330 = margin_trading_all['2330']
    # print 2330 margin purchase
    print(margin_trading_2330.margin_purchase)
    # print 2330 short covering
    print(margin_trading_2330.short_covering)
    # getting 3529 margin trading data in 2020/10/30
    margin_trading_3529 = margin_trading_all['3529']
    # print 3529 margin purchase
    print(margin_trading_3529.margin_purchase)
    # print 3529 short covering
    print(margin_trading_3529.short_covering)

    """ shareholdings """
    # init stock shareholdings object
    stock_shareholdings = StockShareholdings()
    # getting newest shareholdings data
    shareholdings_newest = stock_shareholdings.get_newest()
    # getting level 1 of 0050 shareholdings data form latest release
    print(shareholdings_newest.get('0050')[1])
    # getting 0050 shareholdings data at 2020/11/6
    shareholdings_0050 = stock_shareholdings.get_by_query(code='0050', date_=datetime(2020, 11, 6).date())
    # getting level 15 of 0050 shareholdings data at 2020/11/6
    print(shareholdings_0050[15])

    # update newest stock info
    UpdateStock.main()
