import requests
class CheckPoint:
    def __init__(self):
        self.id=26096
        self.subLemmaId=7373792
        self.newLemmaId=27263
        self.key='银魂'
        self.desc='空知英秋创作的漫画'
        self.title='银魂'
    def check(self,data):
        '''for item in kwargs:
                   if item.id =='id':
                       assert item.'''
        print(data)
        for item in data.items():
            if item[0]=='id':
                assert item[1]==self.id
            elif item[0]=='subLemmaId':
                assert item[1]==self.subLemmaId
            elif item[0]=='newLemmaId':
                assert item[1]==self.newLemmaId
            elif item[0]=='key':
                assert item[1]==self.key
            elif item[0]=='desc':
                assert item[1]==self.desc
            elif item[0]=='title':
                assert item[1]==self.title
            print('Pass!')
def test_checkData():
    checkPoint=CheckPoint()
    searchparams ={'scope':'103','format':'application/json','appid':'379020','bk_key':'银魂'}
    r =requests.get('http://baike.baidu.com/api/openapi/BaikeLemmaCardApi',params=searchparams)
    data =r.json()
    checkPoint.check(data)
if __name__=="__main__":
    test_checkData()