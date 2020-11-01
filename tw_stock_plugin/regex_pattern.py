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


class TradingPattern:
    VALUE_PATTERN = re.compile(r'[+-]*[\d]+[\.]*[\d]+')
    DIFFERENT_PATTERN = re.compile(r'[+-]')