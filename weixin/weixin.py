# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import sys
reload(sys)
import pycurl
sys.setdefaultencoding('utf8')
import StringIO
c=pycurl.Curl()
url="http://weixin.sogou.com/weixin?type=2&ie=utf8&query=%E6%9C%BA%E5%99%A8%E4%B9%8B%E5%BF%83&tsn=0&ft=&et=&interation=&wxid=oIWsFtyH4wzDYSYFwlcMk8znCtfw&usip=almosthuman2014"

import certifi
c.setopt(pycurl.CAINFO, certifi.where())
c.setopt(c.URL, url)
b = StringIO.StringIO()
c.setopt(pycurl.WRITEFUNCTION, b.write)
c.perform()
wbdata = b.getvalue()
data = BeautifulSoup(wbdata, 'lxml')
#wbdata=requests.get(url)
#wbdata1=wbdata.text
print wbdata


