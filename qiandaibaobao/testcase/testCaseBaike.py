# coding:utf-8
from qiandaibaobao.api import baikeApi
from qiandaibaobao.common.restRequest import RestRequest


def test_baike():
    url = baikeApi.url()
    data = baikeApi.data1()
    request = RestRequest()
    result = request.get(url, data)
    baikeApi.check_point(result)


if __name__ == '__main__':
    test_baike()