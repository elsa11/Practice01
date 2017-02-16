import requests
import json
searchparams={'scope':'103','format':'application/json','appid':'379020','bk_key':'银魂'}
r=requests.get('http://baike.baidu.com/api/openapi/BaikeLemmaCardApi',params=searchparams)
print( r.json())
print(type(r.json()))
#将json由dict转换成str
data01 = json.dumps(r.json())
print(type(data01))
#json_str=r.json()
#json_str
print(data01)
returndata=r.json()
#returndata['id'] 可通过这种方式获取joson中的值
print(returndata['id'])
print(type(returndata['id']))
assert returndata['id']==26096
assert returndata['key']=='银魂'