# -*- coding: UTF-8 -*-
# 作废
from bs4 import BeautifulSoup
import sys
import pycurl
import  StringIO
reload(sys)
sys.setdefaultencoding('utf8')
url="http://www.gaokaopai.com/daxue.html"
c = pycurl.Curl()
import certifi

c.setopt(pycurl.CAINFO, certifi.where())
c.setopt(c.URL, url)
b = StringIO.StringIO()
c.setopt(pycurl.WRITEFUNCTION, b.write)
c.perform()
wbdata = b.getvalue()
soup = BeautifulSoup(wbdata, 'lxml')
#print wbdata
links=soup.select("div.tit > h3 > a")
for link in links:
    print link.get_text()+link.get("href")
    c.setopt(pycurl.CAINFO, certifi.where())
    c.setopt(c.URL, link.get("href"))
    b = StringIO.StringIO()
    c.setopt(pycurl.WRITEFUNCTION, b.write)
    c.perform()
    wbdata = b.getvalue()
    soup = BeautifulSoup(wbdata, 'lxml')
