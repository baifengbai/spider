# -*- coding: utf-8 -*
from __future__ import unicode_literals
import sys
import requests
import string
import chardet
import json
reload(sys)
sys.setdefaultencoding("utf-8")
import urllib2
import urllib
url = 'http://api.map.baidu.com/lbsapi/getpoint/'
data ={
    'qt': "s",'c': 131, 'wd': "合肥金地大厦",'rn': "10",
    'ie':"utf - 8", 'oue': "1",
    'fromproduct': "jsapi",
    'res': "api",
    'callback': "BMap._rd._cbk10899",
    'ak': "ptkL5uenat2I7t9PtWv8m1YhdGtNifGs"
}
get_url = url + urllib.urlencode(data)
dta=urllib2.urlopen(urllib2.Request(get_url))
#print dta.read()

wbdata=requests.get("http://api.house.leju.com/api/map/gethouseinfo?return=jsonp&city=hf&hids50628").content
print wbdata
jqq=wbdata[41:-1]
hjson = json.loads(jqq)
print hjson["data"]["50628"]["coordx2"]
print hjson["data"]["55596"]["coordy2"]

#print type(str(wbdata)).encode("utf-8")
#print wbdata.encode("UTF-8")

#print chardet.detect(wbdata)

#url="http://api.map.baidu.com/?qt=s&c=131&wd=%E5%90%88%E8%82%A5%E9%87%91%E5%9C%B0%E5%A4%A7%E5%8E%A6&rn=10&ie=utf-8&oue=1&fromproduct=jsapi&res=api&callback=BMap._rd._cbk10899&ak=E4805d16520de693a3fe707cdc962045"
#wbdata=requests.get(url)
#print wbdata.text