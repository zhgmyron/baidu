#-*- coding: utf-8 -*-

import urllib2
import json
import collections


url = 'http://apis.baidu.com/heweather/weather/free?city='

city = raw_input(u"输入你想查询的城市:")


url = url + city
request = urllib2.Request(url)
request.add_header("apikey", "8f93f1785915eae73fec5f6dca786b5e")
result = urllib2.urlopen(request).read()
info = json.loads(result)
print url
print info

if (info['HeWeather data service 3.0'][0]['status'] !='ok'):
    print info['HeWeather data service 3.0'][0]['status']
else:
    print u"你查询的城市空气质量指数如下："
    print u"city：", info['HeWeather data service 3.0'][0]['basic']['city']
    print u"time：", info['HeWeather data service 3.0'][0]['hourly_forecast'][0]['date']
    print u"cnty：", info['HeWeather data service 3.0'][0]['basic']['cnty']


