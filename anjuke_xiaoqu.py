import urllib
import urllib2
from bs4 import BeautifulSoup
import lxml
import requests
import re
import pycurl

import StringIO
import sys

reload(sys)
sys.setdefaultencoding('utf8')



def info(price,url):
    name=""
    priceE=price
    print url
    c1=pycurl.Curl()
    import certifi
    c1.setopt(pycurl.CAINFO, certifi.where())
    c1.setopt(c1.URL,url)
    b1 = StringIO.StringIO()
    c1.setopt(pycurl.WRITEFUNCTION,b1.write)
    c1.perform()
    wbdata=b1.getvalue()
    #print wbdata
    #print "he"
    data = BeautifulSoup(wbdata, 'lxml')
    rprice=data.select("div.comm-cont > h1")
    for rp in rprice:
        #print rp.text
        name=rp.text

    price=data.select("div.border-info > div.comm-list > dl.comm-l-detail > dd")
    print price.__len__()
    area=price[1].text.strip().replace("/n",'').replace("\n\n",'').replace(" ",'')
    #print repr(area)
    address=price[2].text.strip()
    map=""
    try:
        map = str(price[2]).split("l2")[1].split('&')[0][1:] + ',' + \
              str(price[2]).split("l1")[1].split('&')[0][1:]
    except Exception:
        print "can't find map"
    developer=price[3].text
    propertyCompany=price[4].text
    propertyType=price[5].text
    propertyFee=price[6].text
    #print map
    price2 = data.select("div.border-info > div.comm-list > dl.comm-r-detail > dd")
    print price2.__len__()
    totalHouse=price2[1].text
    voRatio=price2[3].text
    greenRatio=price2[6].text
    new_count=name+'*'+'*'+priceE+'*'+address+'*'+propertyType+'*'+area+'*'+'*'+developer+'*'+'*'+'*'+voRatio+'*'+greenRatio+'*'+totalHouse+'*'+propertyFee+'*'+propertyCompany+'*'+map+"\n"
    print new_count
    f1=file('E:\\hfhouse\\anjuke_xinzhanqu','a+')
    f1.write(new_count)
    f1.close()


def nextpage(url):
    #wbdata=requests.Session().get(url,verify=False)
    #print wbdata.text
    #data=BeautifulSoup(wbdata.text,'lxml')
    #print data

    c=pycurl.Curl()
    import certifi
    c.setopt(pycurl.CAINFO, certifi.where())
    c.setopt(c.URL,url)
    b = StringIO.StringIO()
    c.setopt(pycurl.WRITEFUNCTION,b.write)
    c.perform()
    wbdata=b.getvalue()
    data = BeautifulSoup(wbdata, 'lxml')

    hap=data.select("div.li-itemmod")
    for haps in hap:
        #print haps
        print haps.get("link")
        priceEE=''
        try:
            priceEE=str(haps).split("strong>")[1].split("<")[0]
            print priceEE
        except Exception:
            print "cant find price"
        info(priceEE,"https://hf.anjuke.com" + haps.get("link")[:-1])
'''
    lines=data.select("div.li-itemmod > div.li-info > h3 > a")
    print lines.__len__()
    for line in lines:
        print line.get_text()+line.get("href")
        #info(line.get_text(),"https://hf.anjuke.com"+line.get("href")[:-1])
'''



i=1
while i<10:
    url="https://hf.anjuke.com/community/xinzhanqu/p"+str(i)+"/"
    print url
    nextpage(url)
    i=i+1
