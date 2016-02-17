#-*- coding: utf-8 -*-

import urllib2
import json
import collections


url = 'http://apistore.baidu.com/microservice/aqi?city='

city = raw_input(u"输入你想查询的城市:")


url = url+city

headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)'}
request = urllib2.Request(url,headers=headers)

result = urllib2.urlopen(request).read()
info = json.loads(result,object_pairs_hook=collections.OrderedDict)
print url
print info

if (info['errNum'] == -1):
    print(info['retMsg'])
else:
    print ''
