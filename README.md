# tw-stock-plugin
**Some util function when doing Taiwan stock web scraping and some common stock data parser.**

## What can tw-stock-plugin do?
- Getting newest stock information from official website.
- Getting daily stock trading data from official website.
- Check if the date is open date in stock market.
- Convert specific datetime format more easily.

## How To Use:

### Getting Stock Information
```python
"""
    Attribute:
        - code: 股票代碼
        - name: 股票名稱
        - ISIN_code: 國際證券辨識號碼(ISIN Code)
        - listed_date: 上市/上櫃/興櫃 日
        - category: 市場別
        - industry: 產業別
        - CFI_code: CFICode
"""
from tw_stock_plugin import StockInfo, UpdateStock

# update newest stock info
UpdateStock.main()

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
```

### Check If The Date Is Open Date
```python
from datetime import datetime
from tw_stock_plugin import StockTools

# check if 2020/10/10 is open date, it will return False
print(StockTools.check_is_open_date(datetime.strptime('2020/10/10', '%Y/%m/%d').date()))

# check if 2020/10/23 is open date, it will return True
print(StockTools.check_is_open_date(datetime.strptime('2020/10/23', '%Y/%m/%d').date()))

# check if 2020/10/23 is open date, it will type error because it's not type of datetime.time
print(StockTools.check_is_open_date('2020/03/18'))
```

### Converting Date Between Republic Era And Ad
```python
from tw_stock_plugin import StockTools

# convert 109/10/10 to ad, it allow Y/m/d and Y-m-d format
print(StockTools.republic_era_to_ad(date_='109/10/10'))

# convert 2020/10/10 to republic era, it allow Y/m/d and Y-m-d format
print(StockTools.ad_to_republic_era(date_='2020/10/10'))
```
**this tool is very useful when crawling [tpex](https://www.tpex.org.tw) api.**

### Getting Daily Trading Data
```python
"""
    You can get all day and all stocks data or get only single one stock history data.

    Attribute:
        - Daily Trading Data
            - 上市:
                - code: 股票代碼
                - name: 股票名稱
                - trading_volume: 成交股數
                - transaction: 成交筆數
                - trade_value: 成交金額
                - opening_price: 開盤價
                - highest_price: 最高價
                - lowest_price: 最低價
                - closing_price: 收盤價
                - change: 漲跌價差
                - last_best_bid_price: 最後揭示買價
                - last_best_bid_volume: 最後揭示賣價
                - last_best_ask_price: 最後揭示買量
                - last_best_ask_volume: 最後揭示買量
                - price_earning_rate: 本益比
            - 上櫃:
                - code: 股票代碼
                - name: 股票名稱
                - closing_price: 收盤價
                - change: 漲跌價差
                - opening_price: 開盤價
                - highest_price: 最高價
                - lowest_price: 最低價
                - trading_volume: 成交股數
                - trade_value: 成交金額
                - transaction: 成交筆數
                - last_best_bid_price: 最後揭示買價
                - last_best_ask_price: 最後揭示買量
                - last_best_bid_volume: 最後揭示賣價
                - last_best_ask_volume: 最後揭示買量
                - issued_shares: 發行股數
                - next_limit_up: 次日漲停價
                - next_limit_down: 次日跌停價
         
        - Monthly Trading Data
            - 上市:
                - trading_volume: 成交股數
                - transaction: 成交筆數
                - trade_value: 成交金額
                - opening_price: 開盤價
                - highest_price: 最高價
                - lowest_price: 最低價
                - closing_price: 收盤價
                - change: 漲跌價差
            - 上櫃:
                - closing_price: 收盤價
                - change: 漲跌價差
                - opening_price: 開盤價
                - highest_price: 最高價
                - lowest_price: 最低價
                - trading_volume: 成交股數
                - trade_value: 成交金額
                - transaction: 成交筆數
"""
from datetime import datetime
from tw_stock_plugin.core.stock_trading import StockTrading

# setting target date
date_ = datetime(2020, 10, 30).date()

# init stock trading object with specific date
stock_trading = StockTrading(date_=date_)

# getting all trading data in 2020/10/30
trading_all = stock_trading.get_all()

# getting 2330 trading data in 2020/10/30
trading_2330 = trading_all['2330']

# getting monthly history trading data of 1101 in 2020/10
trading_history_1101 = stock_trading.get_history(code=1101)

# getting monthly history trading data of 9962 in 2020/10
trading_history_9962 = stock_trading.get_history(code=9962)
```
### [Sample Code](https://github.com/chienfeng0719/tw-stock-plugin/blob/develop/example.py)
```python
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
from tw_stock_plugin import StockInfo, StockTrading, StockTools, UpdateStock

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

    # update newest stock info
    UpdateStock.main()
```

---
<a href="https://www.buymeacoffee.com/jimmyyyeh" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-blue.png" alt="Buy Me A Coffee" height="40" width="175"></a>

**Buy me a coffee, if you like it!**
