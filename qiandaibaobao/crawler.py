
from pyquery import PyQuery as pq
p=pq(url='http://www.yinwang.org')
#print(p)
#data=p('.list-group-item title')
lis=p('li').items()
article_list=[]
for li in lis:
    title = li('a').text()
    url = li('a').attr('href')
     #print('文章名称：',li('a').text(),'  ','文章地址：',li('a').attr('href'))
    article = {'title':title,'url':url}
    article_list.append(article)
data = {'articles':article_list}
for iterm in data['articles']:
    print(iterm)

