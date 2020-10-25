# tw-stock-plugin
**Some common function when doing Taiwan stock web scraping.**

## What can tw-stock-plugin do?
- get newest stock information from official website.
- check if the date is open date in stock market.
- convert specific datetime format more easily.

## How To Use:

### Getting Stock Information
```python
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
from tw_stock_plugin import StockInfo, StockTools, UpdateStock

if __name__ == '__main__':

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
```

---
<a href="https://www.buymeacoffee.com/jimmyyyeh" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-blue.png" alt="Buy Me A Coffee" height="40" width="175"></a>

**Buy me a coffee, if you like it!**
