# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf8')

url="https://baike.baidu.com/item/%E6%B8%85%E5%8D%8E%E5%A4%A7%E5%AD%A6/111764"
wbdata=requests.get(url)
wbdata=wbdata.content
soup=BeautifulSoup(wbdata,"lxml")
lines=soup.select(" dl.basicInfo-block > dt.basicInfo-item ")
print lines.__len__()
i = 1
for line in lines:
    print line.get_text()

    print i
    i=i+1
lines=soup.select("dl.basicInfo-block > dd.basicInfo-item")
print lines.__len__()
i = 1
for line in lines:
    print line.get_text()

    print i
    i=i+1