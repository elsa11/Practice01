# coding:utf-8

#result包含expected并值相等
def check_contain_equal(result=None, expected=None):
    for item in expected.items():
        key, value = item
        result_value = result.get(key)
        assert result_value == value, '{}字段的值:{} 不等于预期值:{}'.format(key, result_value, value)
    print('通过')
