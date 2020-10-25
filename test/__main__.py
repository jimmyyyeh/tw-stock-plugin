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
import unittest
import random
from datetime import datetime

from tw_stock_plugin import StockInfo, StockTools, Stock


class TwStockPluginTest(unittest.TestCase):
    def setUp(self):
        self.stock_info = StockInfo()
        self.stock_dict = {
            '2330': {'code': '2330',
                     'name': '台積電',
                     'ISIN_code': 'TW0002330008',
                     'listed_date': '1994/09/05',
                     'category': '上市',
                     'industry': '半導體業',
                     'CFI_code': 'ESVUFR'},
            '8446': {'code': '8446',
                     'name': '華研',
                     'ISIN_code': 'TW0008446006',
                     'listed_date': '2013/12/19',
                     'category': '上櫃',
                     'industry': '文化創意業',
                     'CFI_code': 'ESVUFR'},
            '1269': {'code': '1269',
                     'name': '乾杯',
                     'ISIN_code': 'TW0001269009',
                     'listed_date': '2016/08/29',
                     'category': '興櫃',
                     'industry': '觀光事業',
                     'CFI_code': 'ESVUFR'},
        }
        self.date_convert_dict = {
            '2020/10/10': '109/10/10',
            '2020/01/01': '109/01/01',
            '1996/07/19': '85/07/19',
            '2020-10-10': '109-10-10',
            '2020-01-01': '109-01-01',
            '1996-07-19': '85-07-19'
        }

    def test_get_single(self):
        stock_code = random.choice(list(self.stock_dict))
        stock_info = Stock(**self.stock_dict[stock_code])
        stock_info_test = self.stock_info.get(code=stock_code)
        self.assertEqual(stock_info.__dict__, stock_info_test.__dict__)

    def test_get_stock_attribute(self):
        stock_code = random.choice(list(self.stock_dict))
        stock_info = self.stock_dict[stock_code]
        stock_info_test = self.stock_info.get(code=stock_code)
        for key in stock_info.keys():
            value = stock_info[key]
            value_test = getattr(stock_info_test, key)
            self.assertEqual(value, value_test)

    def test_is_open_date(self):
        open_day_date = datetime.strptime('2020/10/23', '%Y/%m/%d').date()
        holiday_date = datetime.strptime('2020/10/10', '%Y/%m/%d').date()
        self.assertTrue(StockTools.check_is_open_date(open_day_date))
        self.assertFalse(StockTools.check_is_open_date(holiday_date))

    def test_republic_era_to_ad(self):
        ad = random.choice(list(self.date_convert_dict))
        republic_era = self.date_convert_dict[ad]
        self.assertEqual(ad, StockTools.republic_era_to_ad(date_=republic_era))

    def test_ad_to_republic_era(self):
        ad = random.choice(list(self.date_convert_dict))
        republic_era = self.date_convert_dict[ad]
        self.assertEqual(republic_era, StockTools.ad_to_republic_era(date_=ad))


if __name__ == '__main__':
    unittest.main()
