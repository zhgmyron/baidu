#-*- coding: utf-8 -*-

import urllib2
import json
import collections

url = "http://apis.baidu.com/apistore/mobilephoneservice/mobilephone?tel="

tel= raw_input(u"请输入你想查询的手机号：")

url=url + tel

request = urllib2.Request(url)
request.add_header("apikey", "8f93f1785915eae73fec5f6dca786b5e")
result = urllib2.urlopen(request).read()
info = json.loads(result)
print info
print url
if (info['errNum']==-1):
    print (info['errMsg'])
else:
    print (u"你查询的手机信息：")
    print u"tel:",info['retData']['telString']
    print u"province:",info['retData']['province']
    print u"carrier:",info['retData']['carrier']
