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


class ResponseHandler:
    @classmethod
    def get(cls, url, params=None, headers=None, timeout=10):
        response = requests.get(url, params=params, headers=headers, timeout=timeout)
        return response

    @classmethod
    def post(cls, url, params=None, payload=None, headers=None, timeout=10):
        response = requests.post(url=url, params=params, data=payload, headers=headers, timeout=timeout)
        return response
