# coding:utf-8

import requests


class RestRequest(object):
    def __init__(self):
        pass

    def get(self, url, params=None, **kwargs):
        print('>>请求:{},数据{}'.format(url, params))
        data = requests.get(url, params=params, **kwargs).json()
        print('>>响应:{}'.format(data))
        return data

    def post(self, url):
        pass
