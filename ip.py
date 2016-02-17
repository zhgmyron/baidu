#-*- coding: utf-8 -*-

import urllib2
import json
import collections

url = "http://apistore.baidu.com/microservice/iplookup?ip="

ip = raw_input(u"输入你想查询的IP地址:")

url = url + ip
request = urllib2.Request(url)
result = urllib2.urlopen(request).read()
info = json.loads(result,object_pairs_hook=collections.OrderedDict)
print url
print info
if (info['errNum'] == -1):
    print(info['retMsg'])
else:
    print(u"你查询的IP地址信息如下：")
    print u"IP：", info['retData']['ip']
    print u"国家：", info['retData']['country']
    print u"省份：", info['retData']['province']
    print u"城市：", info['retData']['city']
    print u"地点：", info['retData']['district']
    print u"运营商：", info['retData']['carrier']