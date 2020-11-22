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

from datetime import date
from schema import Schema, Or


class SchemaPattern:
    StockInfoSchema = Schema({
        'code': str,
        'name': str,
        'ISIN_code': str,
        'listed_date': str,
        'category': str,
        'industry': Or(str, None),
        'CFI_code': str,
        'type': str
    })

    TwseStockTradingSchema = Schema({
        'code': Or(str, None),
        'name': Or(str, None),
        'closing_price': Or(float, None),
        'change': Or(float, str, None),
        'opening_price': Or(float, None),
        'highest_price': Or(float, None),
        'lowest_price': Or(float, None),
        '_different': Or(str, None),
        'trading_volume': Or(float, None),
        'trade_value': Or(float, None),
        'transaction': Or(float, None),
        'last_best_bid_price': Or(float, None),
        'last_best_ask_price': Or(float, None),
        'last_best_bid_volume': Or(float, None),
        'last_best_ask_volume': Or(float, None),
        'price_earning_rate': Or(float, None),
    })

    TpexStockTradingSchema = Schema(
        {
            'code': Or(str, None),
            'name': Or(str, None),
            'closing_price': Or(float, None),
            'change': Or(float, str, None),
            'opening_price': Or(float, None),
            'highest_price': Or(float, None),
            'lowest_price': Or(float, None),
            'trading_volume': Or(float, None),
            'trade_value': Or(float, None),
            'transaction': Or(float, None),
            'last_best_bid_price': Or(float, None),
            'last_best_ask_price': Or(float, None),
            'last_best_bid_volume': Or(float, None),
            'last_best_ask_volume': Or(float, None),
            'issued_shares': Or(float, None),
            'next_limit_up': Or(float, None),
            'next_limit_down': Or(float, None),
        }
    )

    StockInstitutionalInvestorsSchema = Schema(
        {
            'code': str,
            'name': str,
            'foreign_mainland_area_buy': float,
            'foreign_mainland_area_sell': float,
            'foreign_mainland_area_diff': float,
            'foreign_buy': float,
            'foreign_sell': float,
            'foreign_diff': float,
            'trust_buy': float,
            'trust_sell': float,
            'trust_diff': float,
            'proprietary_dealers_buy': float,
            'proprietary_dealers_sell': float,
            'proprietary_dealers_diff': float,
            'hedge_dealers_buy': float,
            'hedge_dealers_sell': float,
            'hedge_dealers_diff': float,
            'total_diff': float,
        }
    )

    TwseStockMarginTradingSchema = Schema({
        'code': str,
        'name': str,
        'margin_purchase': float,
        'margin_sells': float,
        'cash_redemption': float,
        'cash_balance_of_previous_day': float,
        'cash_balance_of_the_day': float,
        'cash_quota': float,
        'short_covering': float,
        'short_sale': float,
        'stock_redemption': float,
        'stock_balance_of_previous_day': float,
        'stock_balance_of_the_day': float,
        'stock_quota': float,
        'offset': float,
        'note': Or(str, None)}
    )

    TpexStockMarginTradingSchema = Schema({
        'code': str,
        'name': str,
        'cash_balance_of_previous_day': float,
        'margin_purchase': float,
        'margin_sells': float,
        'cash_redemption': float,
        'cash_balance_of_the_day': float,
        'cash_belong_to_securities_finance': float,
        'cash_utilization_rate': float,
        'cash_quota': float,
        'stock_balance_of_previous_day': float,
        'short_covering': float,
        'short_sale': float,
        'stock_redemption': float,
        'stock_balance_of_the_day': float,
        'stock_belong_to_securities_finance': float,
        'stock_utilization_rate': float,
        'stock_quota': float,
        'offset': float,
        'note': Or(str, None)
    })

    StockShareholdingsSchema = Schema({
        'date': date,
        'code': str,
        'index': int,
        'number_of_shares': Or(str, None),
        'number_of_shareholders': int,
        'total_shares': int,
        'percentage_over_total_shares': float
    })

    StockPERatioSchema = Schema({
        'name': Or(str, None),
        'code': Or(str, None),
        'date': Or(date, None),
        'per': Or(float, None),
        'dividend_per_share': Or(float, None),
        'dividend_year': Or(int, None),
        'yield_ratio': Or(float, None),
        'pbr': Or(float, None),
        'fiscal_year_quarter': Or(str, None)
    })
