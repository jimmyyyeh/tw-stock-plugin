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


class DatePattern:
    REPUBLIC_ERA_PATTERN = re.compile(r'\d{2,3}[/-]\d{1,2}[/-]\d{1,2}')  # regex of republic era
    AD_PATTERN = re.compile(r'\d{4}[/-]\d{1,2}[/-]\d{1,2}')  # regex of ad


class StockPattern:
    CODE_NAME_PATTERN = re.compile(r'[\da-zA-Z]+\s.*')


class TradingPattern:
    DIFFERENT_PATTERN = re.compile(r'[\-+X]')


class MarginTradingPattern:
    NOTE_STRIP_PATTERN = re.compile(r'[\s]+')


class PERatioPattern:
    CHINESE_DATE_PATTERN = re.compile(r'([\d]+)年([\d]+)月([\d]+)日')
