# coding:utf-8
from common.check import check_contain_equal


def url():
    return 'http://baike.baidu.com/api/openapi/BaikeLemmaCardApi'


def data1():
    return {'scope': '103', 'format': 'application/json', 'appid': '379020', 'bk_key': '银魂'}


def check_point(result):
    print('this result', result)
    expected = {
        'id': 26096,
        'subLemmaId': 7373792,
        'newLemmaId': 27263,
        'key': '银魂'
    }
    check_contain_equal(result, expected)
