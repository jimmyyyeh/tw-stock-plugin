# tw-stock-plugin
**Some util function when doing Taiwan stock web scraping and some common stock data parser.**

## What can tw-stock-plugin do?
- Getting the newest stock information from the official website.
    - [上市](https://isin.twse.com.tw/isin/C_public.jsp?strMode=2)
    - [上櫃](https://isin.twse.com.tw/isin/C_public.jsp?strMode=4)
    - [興櫃](https://isin.twse.com.tw/isin/C_public.jsp?strMode=5)
- Getting daily stock trading data from the official website.
    - [上市(全)](https://www.twse.com.tw/zh/page/trading/exchange/MI_INDEX.html)
    - [上市(個股)](https://www.twse.com.tw/zh/page/trading/exchange/STOCK_DAY.html)
    - [上櫃(全)](https://www.tpex.org.tw/web/stock/aftertrading/otc_quotes_no1430/stk_wn1430.php?l=zh-tw)
    - [上櫃(個股)](https://www.tpex.org.tw/web/stock/aftertrading/daily_trading_info/st43.php?l=zh-tw)
- Getting daily stock institutional investors data from the official website.
    - [上市](https://www.twse.com.tw/zh/page/trading/fund/T86.html)
    - [上櫃](https://www.tpex.org.tw/web/stock/3insti/daily_trade/3itrade_hedge.php?l=zh-tw)
- Getting daily stock margin trading data from the official website.
    - [上市](https://www.twse.com.tw/zh/page/trading/exchange/MI_MARGN.html)
    - [上櫃](https://www.tpex.org.tw/web/stock/margin_trading/margin_balance/margin_bal.php?l=zh-tw)
- Getting p/e ratio, dividend yield and p/b ratio from the official website.
    - [上市(全)](https://www.twse.com.tw/zh/page/trading/exchange/BWIBBU_d.html)
    - [上市(個股)](https://www.twse.com.tw/zh/page/trading/exchange/BWIBBU.html)
    - [上櫃(全)](https://www.tpex.org.tw/web/stock/aftertrading/peratio_analysis/pera.php?l=zh-tw)
    - [上櫃(個股)](https://www.tpex.org.tw/web/stock/aftertrading/peratio_stk/pera.php?l=zh-tw)
- Getting stock shareholdings data from the official website.
    - [上市/上櫃](https://www.tdcc.com.tw/portal/zh/smWeb/qryStock)
- Check if the date is open date in stock market.
- Convert specific datetime format more easily.

## NOTE
1. The following definition of data and variable are all refer to the official website.
2. To avoiding banned by the official website, I recommend that users who use tw-stock-plugin set delay time at least three seconds after calling each function.
## How To Use:

### Stock Information
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
        - type: 證券類別(股票/ETF...)
"""
from tw_stock_plugin import StockInfo, UpdateStock

# update newest stock info
UpdateStock.main()
# init stock info object
stock_info = StockInfo()
# get all stocks info
print(stock_info.get())
# get 1101 stock info
print(stock_info.get('1101'))
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

### Daily Trading
```python
"""
    You can get all data with specific date or get only single one stock history data.

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

### Institutional Investors
```python
"""
    You can get all data with specific date.

    Attribute:
        - code: 股票代碼
        - name: 股票名稱
        - foreign_mainland_area_buy: 外陸資買進股數(不含外資自營商)
        - foreign_mainland_area_sell: 外陸資賣出股數(不含外資自營商)
        - foreign_mainland_area_diff: 外陸資買賣超股數(不含外資自營商)
        - foreign_buy: 外資自營商買進股數
        - foreign_sell: 外資自營商賣出股數
        - foreign_diff: 外資自營商買賣超股數
        - trust_buy: 投信買進股數
        - trust_sell: 投信賣出股數
        - trust_diff: 投信買賣超股數
        - proprietary_dealers_buy: 自營商買進股數(自行買賣)
        - proprietary_dealers_sell: 自營商賣出股數(自行買賣)
        - proprietary_dealers_diff: 自營商買賣超股數(自行買賣)
        - hedge_dealers_buy: 自營商買進股數(避險)
        - hedge_dealers_sell: 自營商賣出股數(避險)
        - hedge_dealers_diff: 自營商買賣超股數(避險)
        - total_diff: 三大法人買賣超股數
"""
from datetime import datetime
from tw_stock_plugin.core.stock_institutional_investors import StockInstitutionalInvestors

date_ = datetime(2020, 11, 6).date()
# init stock institutional investors object with specific date
stock_institutional_investors = StockInstitutionalInvestors(date_=date_)
# getting all institutional investors data in 2020/10/30
institutional_investors_all = stock_institutional_investors.get_all()
# getting 2330 institutional investors data in 2020/10/30
institutional_investors_2330 = institutional_investors_all['2330']
# getting 3529 institutional investors data in 2020/10/30
institutional_investors_3529 = institutional_investors_all['3529']
```

### Margin Trading
```python
"""
    You can get all data with specific date.
    
    Attribute:
        - 上市:
            - code: 股票代碼
            - name: 股票名稱
            - margin_purchase: 融資買進
            - margin_sells: 融資賣出
            - cash_redemption: 現金償還
            - cash_balance_of_previous_day: 前日餘額
            - cash_balance_of_the_day: 今日餘額
            - cash_quota: 限額
            - short_covering: 融券買進
            - short_sale: 融券賣出
            - stock_redemption: 現金償還
            - stock_balance_of_previous_day: 前日餘額
            - stock_balance_of_the_day: 今日餘額
            - stock_quota: 限額
            - offset: 資券互抵
            - note: 備註
                - 備註欄說明:
                    O：停止融資
                    X：停止融券
                    @：融資分配
                    %：融券分配
                    !：停止買賣
        - 上櫃:
            - code: 股票代碼
            - name: 股票名稱
            - cash_balance_of_previous_day: 前日餘額
            - margin_purchase: 融資買進
            - margin_sells: 融資賣出
            - cash_redemption: 現金償還
            - cash_balance_of_the_day: 今日餘額
            - cash_belong_to_securities_finance: 資屬證金
            - cash_utilization_rate(%): 資使用率(%)
            - cash_quota: 限額
            - stock_balance_of_previous_day: 前日餘額
            - short_covering: 融券買進
            - short_sale: 融券賣出
            - stock_redemption: 現金償還
            - stock_balance_of_the_day: 今日餘額
            - stock_belong_to_securities_finance: 券屬證金
            - stock_utilization_rate(%): 券使用率(%)
            - stock_quota: 限額
            - offset: 資券互抵
            - note: 備註
                - 備註欄說明
                    數字(1、2、3…)：合計降低融資比率、提高融券保證金成數
                    O：停止融資
                    X：停止融券
                    @：融資分配
                    %：融券分配
                    !：停止買賣
                    *：融券餘額占融資餘額百分之六十以上者
                    A：股價波動過度劇烈
                    B：股權過度集中
                    C：成交量過度異常
                    D：監視第二次處置
                    數字(1、2、3…)：監視業務督導會報決議降低融資比率、提高融券保證金成數
"""
from datetime import datetime
from tw_stock_plugin.core.stock_margin_trading import StockMarginTrading

date_ = datetime(2020, 11, 6).date()
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
```

### P/E Ratio
```python
"""
    You can get all data with specific date or get only single one stock history data.

    Attribute:
        - P/E Ratio Data
            - 上市:
                - code: 股票代碼
                - name: 股票名稱
                - yield_ratio: 殖利率(%)
                - dividend_year: 股利年度
                - per: 本益比
                - pbr: 股價淨值比
                - fiscal_year_quarter: 財報年/季
            - 上櫃:
                - code: 股票代碼
                - name: 股票名稱
                - yield_ratio: 殖利率(%)
                - dividend_year: 股利年度
                - per: 本益比
                - pbr: 股價淨值比
                - dividend_per_share: 每股股利

        - Monthly P/E Ratio Data
            - 上市:
                - yield_ratio: 殖利率(%)
                - dividend_year: 股利年度
                - per: 本益比
                - pbr: 股價淨值比
                - fiscal_year_quarter: 財報年/季

            - 上櫃:
                - yield_ratio: 殖利率(%)
                - dividend_year: 股利年度
                - per: 本益比
                - pbr: 股價淨值比
"""
from datetime import datetime
from tw_stock_plugin.core.stock_peratio import StockPERatio

date_ = datetime(2020, 11, 6).date()

# init stock p/e ratio, dividend yield and p/b ratio object with specific date
stock_p_e_ratio = StockPERatio(date_=date_)
# getting all p/e ratio, dividend yield and p/b ratio data in 2020/10/30
p_e_ratio_all = stock_p_e_ratio.get_all()
# getting 2330 p/e ratio, dividend yield and p/b ratio data in 2020/10/30
p_e_ratio_2330 = p_e_ratio_all['2330']
# print 2330 pbr
print(p_e_ratio_2330.pbr)
# print 2330 per
print(p_e_ratio_2330.per)
# getting monthly history p/e ratio, dividend yield and p/b ratio data of 1101 in 2020/10
p_e_ratio_history_1101 = stock_p_e_ratio.get_history(code=1101)
# get only 2020/10/30 p/e ratio, dividend yield and p/b ratio data
print(p_e_ratio_history_1101[date_])
# getting monthly history p/e ratio, dividend yield and p/b ratio data data of 9962 in 2020/10
p_e_ratio_history_9962 = stock_p_e_ratio.get_history(code=9962)
# get only 2020/10/30 p/e ratio, dividend yield and p/b ratio data data
print(p_e_ratio_history_9962[date_])
```

### Shareholdings
```python
"""
    You can get newest data or only specific stock data at specific date.
    
    Attribute:
        - date: 日期
        - code: 股票代碼
        - index: 序
        - number_of_shares: 持股/單位數分級
        - number_of_shareholders: 人數
        - total_shares: 股數/單位數
        - percentage_over_total_shares: 占集保庫存數比例 (%)
"""
from datetime import datetime
from tw_stock_plugin.core.stock_shareholdings import StockShareholdings

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
```

### [Sample Code](https://github.com/jimmyyyeh/tw-stock-plugin/blob/develop/example.py)
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
from tw_stock_plugin import StockInfo, StockTrading, StockInstitutionalInvestors, StockMarginTrading, StockPERatio, \
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

    """ P/E ratio """
    # init stock p/e ratio, dividend yield and p/b ratio object with specific date
    stock_p_e_ratio = StockPERatio(date_=date_)
    # getting all p/e ratio, dividend yield and p/b ratio data in 2020/10/30
    p_e_ratio_all = stock_p_e_ratio.get_all()
    # getting 2330 p/e ratio, dividend yield and p/b ratio data in 2020/10/30
    p_e_ratio_2330 = p_e_ratio_all['2330']
    # print 2330 pbr
    print(p_e_ratio_2330.pbr)
    # print 2330 per
    print(p_e_ratio_2330.per)
    # getting monthly history p/e ratio, dividend yield and p/b ratio data of 1101 in 2020/10
    p_e_ratio_history_1101 = stock_p_e_ratio.get_history(code=1101)
    # get only 2020/10/30 p/e ratio, dividend yield and p/b ratio data
    print(p_e_ratio_history_1101[date_])
    # getting monthly history p/e ratio, dividend yield and p/b ratio data data of 9962 in 2020/10
    p_e_ratio_history_9962 = stock_p_e_ratio.get_history(code=9962)
    # get only 2020/10/30 p/e ratio, dividend yield and p/b ratio data data
    print(p_e_ratio_history_9962[date_])

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
```

---
<a href="https://www.buymeacoffee.com/jimmyyyeh" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-blue.png" alt="Buy Me A Coffee" height="40" width="175"></a>

**Buy me a coffee, if you like it!**
