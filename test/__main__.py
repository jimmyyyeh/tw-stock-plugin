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

from tw_stock_plugin import StockInfo, StockTrading, StockInstitutionalInvestors, StockTools, StockInfoObject


class TwStockPluginTest(unittest.TestCase):
    def setUp(self):
        self.testing_date = datetime(2020, 10, 30).date()
        self.stock_info = StockInfo()
        self.stock_trading = StockTrading(date_=self.testing_date)
        self.stock_institutional_investors = StockInstitutionalInvestors(date_=self.testing_date)
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
        self.trading_history_dict = {
            '2330': {'trading_volume': 49770771,
                     'trade_value': 21614729093,
                     'opening_price': 437,
                     'highest_price': 437,
                     'lowest_price': 432,
                     'closing_price': 432,
                     'change': -5,
                     'transaction': 46871},
            '1101': {'trading_volume': 8723616,
                     'trade_value': 353231776,
                     'opening_price': 40.35,
                     'highest_price': 40.60,
                     'lowest_price': 40.30,
                     'closing_price': 40.55,
                     'change': 0.2,
                     'transaction': 2925},
            '9962': {'trading_volume': 59000,
                     'trade_value': 536000,
                     'opening_price': 9.02,
                     'highest_price': 9.11,
                     'lowest_price': 8.91,
                     'closing_price': 9.11,
                     'change': 0.09,
                     'transaction': 22}
        }
        self.trading_all_dict = {
            '1101': {'code': '1101',
                     'name': '台泥',
                     'trading_volume': 8723616,
                     'transaction': 2925,
                     'trade_value': 353231776,
                     'opening_price': 40.35,
                     'highest_price': 40.6,
                     'lowest_price': 40.3,
                     'closing_price': 40.55,
                     'change': 0.2,
                     'last_best_bid_price': 40.5,
                     'last_best_bid_volume': 59,
                     'last_best_ask_price': 40.55,
                     'last_best_ask_volume': 145,
                     'price_earning_rate': 9.56},
            '2330': {'code': '2330',
                     'name': '台積電',
                     'trading_volume': 49770771,
                     'transaction': 46871,
                     'trade_value': 21614729093,
                     'opening_price': 437,
                     'highest_price': 437,
                     'lowest_price': 432,
                     'closing_price': 432,
                     'change': -5,
                     'last_best_bid_price': 432,
                     'last_best_bid_volume': 1338,
                     'last_best_ask_price': 432.50,
                     'last_best_ask_volume': 3,
                     'price_earning_rate': 24.63},
            '1258': {'code': '1258',
                     'name': '其祥-KY',
                     'closing_price': 12.80,
                     'change': -0.3,
                     'opening_price': 12.8,
                     'highest_price': 12.8,
                     'lowest_price': 12.8,
                     'trading_volume': 2000,
                     'trade_value': 25600,
                     'transaction': 2,
                     'last_best_bid_price': 12.8,
                     'last_best_bid_volume': 3000,
                     'last_best_ask_price': 13.1,
                     'last_best_ask_volume': 1000,
                     'issued_shares': 36819791,
                     'next_limit_up': 14.05,
                     'next_limit_down': 11.55}
        }
        self.institutional_investors_all_dict = {
            '1101': {'code': '1101',
                     'name': '台泥',
                     'foreign_mainland_area_buy': 5474400,
                     'foreign_mainland_area_sell': 4865925,
                     'foreign_mainland_area_diff': 608475,
                     'foreign_buy': 0,
                     'foreign_sell': 0,
                     'foreign_diff': 0,
                     'trust_buy': 0,
                     'trust_sell': 0,
                     'trust_diff': 0,
                     'proprietary_dealers_buy': 14000,
                     'proprietary_dealers_sell': 516000,
                     'proprietary_dealers_diff': -502000,
                     'hedge_dealers_buy': 835000,
                     'hedge_dealers_sell': 79000,
                     'hedge_dealers_diff': 756000,
                     'total_diff': 862475},
            '2330': {'code': '2330',
                     'name': '台積電',
                     'foreign_mainland_area_buy': 19943461,
                     'foreign_mainland_area_sell': 39095735,
                     'foreign_mainland_area_diff': -19152274,
                     'foreign_buy': 0,
                     'foreign_sell': 0,
                     'foreign_diff': 0,
                     'trust_buy': 30000,
                     'trust_sell': 46000,
                     'trust_diff': -16000,
                     'proprietary_dealers_buy': 75000,
                     'proprietary_dealers_sell': 1197000,
                     'proprietary_dealers_diff': -1122000,
                     'hedge_dealers_buy': 174000,
                     'hedge_dealers_sell': 431998,
                     'hedge_dealers_diff': -257998,
                     'total_diff': -20548272},
            '3260': {'code': '3260',
                     'name': '威剛',
                     'foreign_mainland_area_buy': 105000,
                     'foreign_mainland_area_sell': 285000,
                     'foreign_mainland_area_diff': -180000,
                     'foreign_buy': 0,
                     'foreign_sell': 0,
                     'foreign_diff': 0,
                     'trust_buy': 0,
                     'trust_sell': 0,
                     'trust_diff': 0,
                     'proprietary_dealers_buy': 14000,
                     'proprietary_dealers_sell': 30000,
                     'proprietary_dealers_diff': -16000,
                     'hedge_dealers_buy': 2000,
                     'hedge_dealers_sell': 18000,
                     'hedge_dealers_diff': -16000,
                     'total_diff': -212000}
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
        stock_info = StockInfoObject(**self.stock_dict[stock_code])
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

    def test_trading_data_history(self):
        stock_code = random.choice(list(self.trading_history_dict))
        stock_trading_history = self.trading_history_dict[stock_code]
        stock_trading_history_test = self.stock_trading.get_history(code=stock_code)[self.testing_date]
        for key in stock_trading_history.keys():
            value = stock_trading_history[key]
            value_test = getattr(stock_trading_history_test, key)
            self.assertEqual(value, value_test)

    def test_trading_data_all(self):
        stock_code = random.choice(list(self.trading_all_dict))
        stock_trading_all = self.trading_all_dict[stock_code]
        stock_trading_all_test = self.stock_trading.get_all()[stock_code]
        for key in stock_trading_all.keys():
            value = stock_trading_all[key]
            value_test = getattr(stock_trading_all_test, key)
            self.assertEqual(value, value_test)

    def test_institutional_investors_data_all(self):
        stock_code = random.choice(list(self.institutional_investors_all_dict))
        stock_institutional_investors_all = self.institutional_investors_all_dict[stock_code]
        stock_institutional_investors_all_test = self.stock_institutional_investors.get_all()[stock_code]
        for key in stock_institutional_investors_all.keys():
            value = stock_institutional_investors_all[key]
            value_test = getattr(stock_institutional_investors_all_test, key)
            self.assertEqual(value, value_test)


if __name__ == '__main__':
    unittest.main()
