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

from datetime import datetime, date

from tw_stock_plugin.regex_pattern import DatePattern
from tw_stock_plugin.constant import Domain
from tw_stock_plugin.utils.response_handler import ResponseHandler


class StockTools:

    @classmethod
    def check_is_open_date(cls, date_):
        """
        check if input date is open date (available in after-hour time)
        :param date_:
        :return:
        """
        if not isinstance(date_, date):
            raise TypeError('input date must be type of datetime.date')
        if date_ > datetime.now().date():
            raise AttributeError('The input date must earlier than today.'.format(date))

        query_date = cls.ad_to_republic_era(date_=date_).replace('-', '/')
        url = f'{Domain.TAIPEI_EXCHANGE}/web/stock/aftertrading/index_summary/summary_result.php'
        params = {'l': 'zh-tw',
                  'd': query_date}
        response = ResponseHandler.get(url=url, params=params)
        json_data = response.json()['aaData']
        if json_data:
            return True
        else:
            return False

    @classmethod
    def ad_to_republic_era(cls, date_):
        """
        convert ad to republic era
            - 2020/10/10 -> 109/10/10
        :param date_:
        :return:
        """
        if isinstance(date_, date):
            date_ = date_.strftime('%Y-%m-%d')

        if DatePattern.AD_PATTERN.fullmatch(date_) and '/' in date_:
            year, month, day = date_.split('/')
            return '{}/{:02d}/{:02d}'.format(int(year) - 1911,
                                             int(month),
                                             int(day))
        elif DatePattern.AD_PATTERN.fullmatch(date_) and '-' in date_:
            year, month, day = date_.split('-')
            return '{}-{:02d}-{:02d}'.format(int(year) - 1911,
                                             int(month),
                                             int(day))
        else:
            raise ValueError('date format error, it is not ad format')

    @classmethod
    def republic_era_to_ad(cls, date_):
        """
        convert republic era to ad
            - 109/10/10 -> 2020/10/10
        :param date_:
        :return:
        """
        if DatePattern.REPUBLIC_ERA_PATTERN.fullmatch(date_) and '/' in date_:
            year, month, day = date_.split('/')
            return '{}/{:02d}/{:02d}'.format(int(year) + 1911,
                                             int(month),
                                             int(day))
        elif DatePattern.REPUBLIC_ERA_PATTERN.fullmatch(date_) and '-' in date_:
            year, month, day = date_.split('-')
            return '{}-{:02d}-{:02d}'.format(int(year) + 1911,
                                             int(month),
                                             int(day))
        else:
            raise ValueError('date format error, it is not republic era format')
