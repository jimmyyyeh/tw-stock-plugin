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

import re
import requests
from datetime import datetime, date


class StockTools:
    _REPUBLIC_ERA_PATTERN = re.compile(r'\d{2,3}[/-]\d{1,2}[/-]\d{1,2}')  # regex of republic era
    _AD_PATTERN = re.compile(r'\d{4}[/-]\d{1,2}[/-]\d{1,2}')  # regex of ad

    @classmethod
    def check_is_open_date(cls, date_):
        """
        check if input date is open date
        :param date_:
        :return:
        """
        if not isinstance(date_, date):
            raise TypeError('input date must be type of datetime.date')
        url = 'https://mis.twse.com.tw/stock/data/futures_side.txt'
        response = requests.get(url)
        json_data = response.json()
        msg_array = json_data['msgArray']
        msg = msg_array[0]
        json_date = msg['d']
        json_date = datetime.strptime(json_date, '%Y%m%d')
        return json_date.date() == date_

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

        if cls._AD_PATTERN.fullmatch(date_) and '/' in date_:
            year, month, day = date_.split('/')
            return '{}/{:02d}/{:02d}'.format(int(year) - 1911,
                                             int(month),
                                             int(day))
        elif cls._AD_PATTERN.fullmatch(date_) and '-' in date_:
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
        if cls._REPUBLIC_ERA_PATTERN.fullmatch(date_) and '/' in date_:
            year, month, day = date_.split('/')
            return '{}/{:02d}/{:02d}'.format(int(year) + 1911,
                                             int(month),
                                             int(day))
        elif cls._REPUBLIC_ERA_PATTERN.fullmatch(date_) and '-' in date_:
            year, month, day = date_.split('-')
            return '{}-{:02d}-{:02d}'.format(int(year) + 1911,
                                             int(month),
                                             int(day))
        else:
            raise ValueError('date format error, it is not republic era format')
