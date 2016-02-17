#-*- coding: utf-8 -*-

import urllib2
import json
import collections

url = "http://apistore.baidu.com/microservice/icardinfo?id="

id_card= raw_input(u"请输入你想查询的身份证号：")

url=url + id_card

request = urllib2.Request(url)
result = urllib2.urlopen(request).read()
info = json.loads(result,object_pairs_hook=collections.OrderedDict)
print info
print url
if (info['errNum']==-1):
    print (info['retMsg'])
else:
    print (u"你查询的身份证信息：")
    print "location:",info['retData']['address']
    print "sex:",info['retData']['sex']
    print "birthday:",info['retData']['birthday']