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
        for _ in range(5):
            try:
                response = requests.get(url, params=params, headers=headers, timeout=timeout)
                return response
            except Exception as e:
                print(str(e))

    @classmethod
    def post(cls, url, params=None, payload=None, headers=None, timeout=10):
        for _ in range(5):
            try:
                response = requests.post(url=url, params=params, data=payload, headers=headers, timeout=timeout)
                return response
            except Exception as e:
                print(str(e))
