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
import requests
from datetime import datetime, date


class StockTools:
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
