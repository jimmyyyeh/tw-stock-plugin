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
from time import sleep

from tw_stock_plugin import StockInfo, StockTrading, StockInstitutionalInvestors, StockMarginTrading, \
    StockPERatio, StockShareholdings, StockTools, StockInfoObject


class TwStockPluginTest(unittest.TestCase):
    def setUp(self):
        self.testing_date = datetime(2020, 10, 30).date()
        self.stock_info = StockInfo()
        self.stock_trading = StockTrading(date_=self.testing_date)
        self.stock_institutional_investors = StockInstitutionalInvestors(date_=self.testing_date)
        self.stock_margin_trading = StockMarginTrading(date_=self.testing_date)
        self.stock_p_e_ratio = StockPERatio(date_=self.testing_date)
        self.stock_dict = {
            '2330': {'code': '2330',
                     'name': '台積電',
                     'ISIN_code': 'TW0002330008',
                     'listed_date': '1994/09/05',
                     'category': '上市',
                     'industry': '半導體業',
                     'CFI_code': 'ESVUFR',
                     'type': '股票'},
            '8446': {'code': '8446',
                     'name': '華研',
                     'ISIN_code': 'TW0008446006',
                     'listed_date': '2013/12/19',
                     'category': '上櫃',
                     'industry': '文化創意業',
                     'CFI_code': 'ESVUFR',
                     'type': '股票'},
            '1269': {'code': '1269',
                     'name': '乾杯',
                     'ISIN_code': 'TW0001269009',
                     'listed_date': '2016/08/29',
                     'category': '興櫃',
                     'industry': '觀光事業',
                     'CFI_code': 'ESVUFR',
                     'type': '股票'},
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
        self.margin_trading_all_dict = {
            '1101': {
                'code': '1101',
                'name': '台泥',
                'margin_purchase': 42,
                'margin_sells': 93,
                'cash_redemption': 0,
                'cash_balance_of_previous_day': 9568,
                'cash_balance_of_the_day': 9517,
                'cash_quota': 1434625,
                'short_covering': 0,
                'short_sale': 17,
                'stock_redemption': 0,
                'stock_balance_of_previous_day': 178,
                'stock_balance_of_the_day': 195,
                'stock_quota': 1434625,
                'offset': 0,
                'note': None
            },
            '00672L': {
                'code': '00672L',
                'name': '元大S&P原油正2',
                'margin_purchase': 0,
                'margin_sells': 0,
                'cash_redemption': 235,
                'cash_balance_of_previous_day': 950,
                'cash_balance_of_the_day': 715,
                'cash_quota': 0,
                'short_covering': 0,
                'short_sale': 0,
                'stock_redemption': 1,
                'stock_balance_of_previous_day': 1,
                'stock_balance_of_the_day': 0,
                'stock_quota': 0,
                'offset': 0,
                'note': 'OX'
            },
            '1595': {
                'code': '1595',
                'name': '川寶',
                'cash_balance_of_previous_day': 194,
                'margin_purchase': 0,
                'margin_sells': 3,
                'cash_redemption': 0,
                'cash_balance_of_the_day': 191,
                'cash_belong_to_securities_finance': 6,
                'cash_utilization_rate': 1.62,
                'cash_quota': 11787,
                'stock_balance_of_previous_day': 0,
                'short_covering': 0,
                'short_sale': 0,
                'stock_redemption': 0,
                'stock_balance_of_the_day': 0,
                'stock_belong_to_securities_finance': 0,
                'stock_utilization_rate': 0,
                'stock_quota': 11787,
                'offset': 0,
                'note': '11,C'
            }
        }
        self.p_e_ratio_history_dict = {
            '2330': {'yield_ratio': 2.2,
                     'dividend_year': 108,
                     'per': 24.63,
                     'pbr': 6.51,
                     'fiscal_year_quarter': '109/2'},
            '1101': {'yield_ratio': 7.40,
                     'dividend_year': 108,
                     'per': 9.56,
                     'pbr': 1.25,
                     'fiscal_year_quarter': '109/2'},
            '9962': {'per': None,
                     'yield_ratio': 2.2,
                     'dividend_year': 108,
                     'pbr': 0.89}
        }
        self.p_e_ratio_all_dict = {
            '1101': {'code': '1101',
                     'name': '台泥',
                     'yield_ratio': 7.4,
                     'dividend_year': 108,
                     'per': 9.56,
                     'pbr': 1.25,
                     'fiscal_year_quarter': '109/2'},
            '2330': {'code': '2330',
                     'name': '台積電',
                     'yield_ratio': 2.2,
                     'dividend_year': 108,
                     'per': 24.63,
                     'pbr': 6.51,
                     'fiscal_year_quarter': '109/2'},
            '2221': {'code': '2221',
                     'name': '大甲',
                     'per': 13.82,
                     'dividend_per_share': 1.5,
                     'dividend_year': 108,
                     'yield_ratio': 6.38,
                     'pbr': 1.33}
        }
        self.shareholdings_dict = {
            1: {'code': '0050',
                'date': datetime(2020, 11, 6).date(),
                'index': 1,
                'number_of_shareholders': 78300,
                'number_of_shares': '1-999',
                'percentage_over_total_shares': 1.92,
                'total_shares': 17839119},
            2: {'code': '0050',
                'date': datetime(2020, 11, 6).date(),
                'index': 2,
                'number_of_shareholders': 77229,
                'number_of_shares': '1000-5000',
                'percentage_over_total_shares': 15.55,
                'total_shares': 143973016},
            3: {'code': '0050',
                'date': datetime(2020, 11, 6).date(),
                'index': 3,
                'number_of_shareholders': 7311,
                'number_of_shares': '5001-10000',
                'percentage_over_total_shares': 6.06,
                'total_shares': 56155961},
            4: {'code': '0050',
                'date': datetime(2020, 11, 6).date(),
                'index': 4,
                'number_of_shareholders': 1974,
                'number_of_shares': '10001-15000',
                'percentage_over_total_shares': 2.72,
                'total_shares': 25262584},
            5: {'code': '0050',
                'date': datetime(2020, 11, 6).date(),
                'index': 5,
                'number_of_shareholders': 1083,
                'number_of_shares': '15001-20000',
                'percentage_over_total_shares': 2.14,
                'total_shares': 19811145},
            6: {'code': '0050',
                'date': datetime(2020, 11, 6).date(),
                'index': 6,
                'number_of_shareholders': 866,
                'number_of_shares': '20001-30000',
                'percentage_over_total_shares': 2.36,
                'total_shares': 21886879},
            7: {'code': '0050',
                'date': datetime(2020, 11, 6).date(),
                'index': 7,
                'number_of_shareholders': 378,
                'number_of_shares': '30001-40000',
                'percentage_over_total_shares': 1.44,
                'total_shares': 13356254},
            8: {'code': '0050',
                'date': datetime(2020, 11, 6).date(),
                'index': 8,
                'number_of_shareholders': 211,
                'number_of_shares': '40001-50000',
                'percentage_over_total_shares': 1.05,
                'total_shares': 9763707},
            9: {'code': '0050',
                'date': datetime(2020, 11, 6).date(),
                'index': 9,
                'number_of_shareholders': 372,
                'number_of_shares': '50001-100000',
                'percentage_over_total_shares': 2.85,
                'total_shares': 26397673},
            10: {'code': '0050',
                 'date': datetime(2020, 11, 6).date(),
                 'index': 10,
                 'number_of_shareholders': 132,
                 'number_of_shares': '100001-200000',
                 'percentage_over_total_shares': 1.96,
                 'total_shares': 18216225},
            11: {'code': '0050',
                 'date': datetime(2020, 11, 6).date(),
                 'index': 11,
                 'number_of_shareholders': 69,
                 'number_of_shares': '200001-400000',
                 'percentage_over_total_shares': 2.17,
                 'total_shares': 20105691},
            12: {'code': '0050',
                 'date': datetime(2020, 11, 6).date(),
                 'index': 12,
                 'number_of_shareholders': 14,
                 'number_of_shares': '400001-600000',
                 'percentage_over_total_shares': 0.74,
                 'total_shares': 6887616},
            13: {'code': '0050',
                 'date': datetime(2020, 11, 6).date(),
                 'index': 13,
                 'number_of_shareholders': 9,
                 'number_of_shares': '600001-800000',
                 'percentage_over_total_shares': 0.69,
                 'total_shares': 6452000},
            14: {'code': '0050',
                 'date': datetime(2020, 11, 6).date(),
                 'index': 14,
                 'number_of_shareholders': 9,
                 'number_of_shares': '800001-1000000',
                 'percentage_over_total_shares': 0.91,
                 'total_shares': 8434000},
            15: {'code': '0050',
                 'date': datetime(2020, 11, 6).date(),
                 'index': 15,
                 'number_of_shareholders': 55,
                 'number_of_shares': '1,000,001以上',
                 'percentage_over_total_shares': 57.36,
                 'total_shares': 530958130}
        }
        self.shareholdings_dict_all = {
            1: {'code': '0050',
                'date': datetime(2020, 11, 13).date(),
                'index': 1,
                'number_of_shareholders': 80620,
                'number_of_shares': '1-999',
                'percentage_over_total_shares': 1.95,
                'total_shares': 18159107},
            2: {'code': '0050',
                'date': datetime(2020, 11, 13).date(),
                'index': 2,
                'number_of_shareholders': 74015,
                'number_of_shares': '1,000-5,000',
                'percentage_over_total_shares': 14.81,
                'total_shares': 137930474},
            3: {'code': '0050',
                'date': datetime(2020, 11, 13).date(),
                'index': 3,
                'number_of_shareholders': 6953,
                'number_of_shares': '5,001-10,000',
                'percentage_over_total_shares': 5.73,
                'total_shares': 53365960},
            4: {'code': '0050',
                'date': datetime(2020, 11, 13).date(),
                'index': 4,
                'number_of_shareholders': 1902,
                'number_of_shares': '10,001-15,000',
                'percentage_over_total_shares': 2.61,
                'total_shares': 24308986},
            5: {'code': '0050',
                'date': datetime(2020, 11, 13).date(),
                'index': 5,
                'number_of_shareholders': 1021,
                'number_of_shares': '15,001-20,000',
                'percentage_over_total_shares': 2.0,
                'total_shares': 18634713},
            6: {'code': '0050',
                'date': datetime(2020, 11, 13).date(),
                'index': 6,
                'number_of_shareholders': 822,
                'number_of_shares': '20,001-30,000',
                'percentage_over_total_shares': 2.22,
                'total_shares': 20754627},
            7: {'code': '0050',
                'date': datetime(2020, 11, 13).date(),
                'index': 7,
                'number_of_shareholders': 344,
                'number_of_shares': '30,001-40,000',
                'percentage_over_total_shares': 1.3,
                'total_shares': 12161242},
            8: {'code': '0050',
                'date': datetime(2020, 11, 13).date(),
                'index': 8,
                'number_of_shareholders': 210,
                'number_of_shares': '40,001-50,000',
                'percentage_over_total_shares': 1.04,
                'total_shares': 9721246},
            9: {'code': '0050',
                'date': datetime(2020, 11, 13).date(),
                'index': 9,
                'number_of_shareholders': 355,
                'number_of_shares': '50,001-100,000',
                'percentage_over_total_shares': 2.7,
                'total_shares': 25229118},
            10: {'code': '0050',
                 'date': datetime(2020, 11, 13).date(),
                 'index': 10,
                 'number_of_shareholders': 128,
                 'number_of_shares': '100,001-200,000',
                 'percentage_over_total_shares': 1.89,
                 'total_shares': 17683736},
            11: {'code': '0050',
                 'date': datetime(2020, 11, 13).date(),
                 'index': 11,
                 'number_of_shareholders': 68,
                 'number_of_shares': '200,001-400,000',
                 'percentage_over_total_shares': 2.12,
                 'total_shares': 19824803},
            12: {'code': '0050',
                 'date': datetime(2020, 11, 13).date(),
                 'index': 12,
                 'number_of_shareholders': 16,
                 'number_of_shares': '400,001-600,000',
                 'percentage_over_total_shares': 0.82,
                 'total_shares': 7722616},
            13: {'code': '0050',
                 'date': datetime(2020, 11, 13).date(),
                 'index': 13,
                 'number_of_shareholders': 6,
                 'number_of_shares': '600,001-800,000',
                 'percentage_over_total_shares': 0.46,
                 'total_shares': 4310000},
            14: {'code': '0050',
                 'date': datetime(2020, 11, 13).date(),
                 'index': 14,
                 'number_of_shareholders': 10,
                 'number_of_shares': '800,001-1,000,000',
                 'percentage_over_total_shares': 0.96,
                 'total_shares': 9001000},
            15: {'code': '0050',
                 'date': datetime(2020, 11, 13).date(),
                 'index': 15,
                 'number_of_shareholders': 56,
                 'number_of_shares': '1,000,001以上',
                 'percentage_over_total_shares': 59.31,
                 'total_shares': 552192372}}
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
        sleep(3)

    def test_get_stock_attribute(self):
        stock_code = random.choice(list(self.stock_dict))
        stock_info = self.stock_dict[stock_code]
        stock_info_test = self.stock_info.get(code=stock_code)
        for key in stock_info.keys():
            value = stock_info[key]
            value_test = getattr(stock_info_test, key)
            self.assertEqual(value, value_test)
        sleep(3)

    def test_is_open_date(self):
        open_day_date = datetime.strptime('2020/10/23', '%Y/%m/%d').date()
        holiday_date = datetime.strptime('2020/10/10', '%Y/%m/%d').date()
        self.assertTrue(StockTools.check_is_open_date(open_day_date))
        self.assertFalse(StockTools.check_is_open_date(holiday_date))
        sleep(3)

    def test_republic_era_to_ad(self):
        ad = random.choice(list(self.date_convert_dict))
        republic_era = self.date_convert_dict[ad]
        self.assertEqual(ad, StockTools.republic_era_to_ad(date_=republic_era))
        sleep(3)

    def test_ad_to_republic_era(self):
        ad = random.choice(list(self.date_convert_dict))
        republic_era = self.date_convert_dict[ad]
        self.assertEqual(republic_era, StockTools.ad_to_republic_era(date_=ad))
        sleep(3)

    def test_trading_data_history(self):
        stock_code = random.choice(list(self.trading_history_dict))
        stock_trading_history = self.trading_history_dict[stock_code]
        stock_trading_history_test = self.stock_trading.get_history(code=stock_code)[self.testing_date]
        for key in stock_trading_history.keys():
            value = stock_trading_history[key]
            value_test = getattr(stock_trading_history_test, key)
            self.assertEqual(value, value_test)
        sleep(3)

    def test_trading_data_all(self):
        stock_code = random.choice(list(self.trading_all_dict))
        stock_trading_all = self.trading_all_dict[stock_code]
        stock_trading_all_test = self.stock_trading.get_all()[stock_code]
        for key in stock_trading_all.keys():
            value = stock_trading_all[key]
            value_test = getattr(stock_trading_all_test, key)
            self.assertEqual(value, value_test)
        sleep(3)

    def test_institutional_investors_data_all(self):
        stock_code = random.choice(list(self.institutional_investors_all_dict))
        stock_institutional_investors_all = self.institutional_investors_all_dict[stock_code]
        stock_institutional_investors_all_test = self.stock_institutional_investors.get_all()[stock_code]
        for key in stock_institutional_investors_all.keys():
            value = stock_institutional_investors_all[key]
            value_test = getattr(stock_institutional_investors_all_test, key)
            self.assertEqual(value, value_test)
        sleep(3)

    def test_margin_trading_data_all(self):
        stock_code = random.choice(list(self.margin_trading_all_dict))
        stock_margin_trading_all = self.margin_trading_all_dict[stock_code]
        stock_margin_trading_all_test = self.stock_margin_trading.get_all()[stock_code]
        for key in stock_margin_trading_all.keys():
            value = stock_margin_trading_all[key]
            value_test = getattr(stock_margin_trading_all_test, key)
            self.assertEqual(value, value_test)
        sleep(3)

    def test_p_e_ratio_data_history(self):
        stock_code = random.choice(list(self.p_e_ratio_history_dict))
        stock_p_e_ratio = self.p_e_ratio_history_dict[stock_code]
        stock_p_e_ratio_test = self.stock_p_e_ratio.get_history(code=stock_code)[self.testing_date]
        for key in stock_p_e_ratio.keys():
            value = stock_p_e_ratio[key]
            value_test = getattr(stock_p_e_ratio_test, key)
            self.assertEqual(value, value_test)
        sleep(3)

    def test_p_e_ratio_data_all(self):
        stock_code = random.choice(list(self.p_e_ratio_all_dict))
        stock_p_e_ratio_all = self.p_e_ratio_all_dict[stock_code]
        stock_p_e_ratio_all_test = self.stock_p_e_ratio.get_all()[stock_code]
        for key in stock_p_e_ratio_all.keys():
            value = stock_p_e_ratio_all[key]
            value_test = getattr(stock_p_e_ratio_all_test, key)
            self.assertEqual(value, value_test)
        sleep(3)

    def test_shareholdings_data(self):
        stock_code = '0050'
        date_ = datetime(2020, 11, 6).date()
        stock_shareholdings = StockShareholdings()
        stock_shareholdings_test = stock_shareholdings.get_by_query(code=stock_code,
                                                                    date_=date_)
        for index in self.shareholdings_dict.keys():
            dict_ = self.shareholdings_dict[index]
            dict_test = stock_shareholdings_test[index]
            for key in dict_.keys():
                value = dict_[key]
                value_test = getattr(dict_test, key)
                self.assertEqual(value, value_test)
        sleep(3)

    # def test_shareholdings_data_all(self):
    #     stock_code = '0050'
    #     stock_shareholdings = StockShareholdings()
    #     stock_shareholdings_test = stock_shareholdings.get_newest()[stock_code]
    #     for index in self.shareholdings_dict_all.keys():
    #         dict_ = self.shareholdings_dict_all[index]
    #         dict_test = stock_shareholdings_test[index]
    #         for key in dict_.keys():
    #             value = dict_[key]
    #             value_test = getattr(dict_test, key)
    #             self.assertEqual(value, value_test)
    #     sleep(3)


if __name__ == '__main__':
    unittest.main()
