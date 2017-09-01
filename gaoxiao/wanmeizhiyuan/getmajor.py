# -*- coding: utf-8 -*
# 喜喜喜喜喜喜
from bs4 import BeautifulSoup
import urllib
import urllib2
import cookielib
import sys
import time
from random import choice
import imp
B=imp.load_source('B','C:\\Users\\Administrator\\PycharmProjects\\spiders\\IP\\ttIP.py')
reload(sys)
sys.setdefaultencoding('utf8')

def getZZ(name,url,list):
    time.sleep(2)
    url='https://www.wmzy.com'+url
    try:
        print choice(list)
        proxy_handler = urllib2.ProxyHandler({"http": choice(list)})
        opener = urllib2.build_opener(proxy_handler)
        request = urllib2.Request(url)
        response = opener.open(request)
    except Exception:
        print choice(list)
        time.sleep(10)
        proxy_handler = urllib2.ProxyHandler({"http": choice(list)})
        opener = urllib2.build_opener(proxy_handler)
        request = urllib2.Request(url)
        response = opener.open(request)
    #print response.read()
    soup=BeautifulSoup(response.read(),'lxml')
    lines=soup.select("div.m-major-product")
    print lines.__len__()
    for line in lines:
        if line.get_text().replace("\n",'').replace(" ", '')=="暂无":
            continue
    response.close()


url='https://www.wmzy.com/api/school/major'
request = urllib2.Request(url)
response = urllib2.urlopen(request)
#print response.read()
soup=BeautifulSoup(response.read(),'lxml')
lines=soup.select(' ul.clear > li > a ')
print lines.__len__()
list=B.getIP().getIPlist()
print list
for line in range(476,lines.__len__()):
    print line
    print lines[line].get_text().replace("\n",'').replace(" ",'')
    #print lines[line].get('href')
    try:
        getZZ(lines[line].get_text().replace("\n",'').replace(" ",''), lines[line].get('href'),list)
    except Exception:
        pass