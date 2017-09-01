# -*- coding: utf-8 -*
import urllib
import urllib2
from bs4 import BeautifulSoup
import lxml
import requests
import re
import sys
import repr
reload(sys)
sys.setdefaultencoding('utf8')
def getdata(url,name):
    #print name+url
    name=name#楼盘
    nickname=name#别名
    priceE="待定"#价格
    address=""#地址
    propertyType=""#物业类别
    loopP=""#环线位置
    developer=""#开发商
    mainUnit=""#主力户型
    school=""
    voRatio=""#容积率
    greenRatio=""#绿化率
    totalHouse=""#总户数
    propertyFee=""#物业费
    propertyCompany=""
    #data={name,nickname,priceE,address,propertyType,loopP, developer,mainUnit,school,voRatio,greenRatio,totalHouse, propertyFee,propertyCompany}
    wbdata1 = requests.get(url)
    wbdata1.encoding = "gb2312"
    wbdata1 = wbdata1.text
    #print wbdata1
    # html=response.read()
    soup1 = BeautifulSoup(wbdata1, 'lxml')
    more=soup1.select(" div.information > div.information_li > div.fl > p > a ")
    for n in more:
        wbdata2 = requests.get(n.get("href"))
        wbdata2.encoding = "gb2312"
        wbdata2 = wbdata2.text
        dataSoup=BeautifulSoup(wbdata2,'lxml')
        #print wbdata2
        price=dataSoup.select(" div.main-info-price > em ")#priceE
        for pricet in price:
            #print pricet.get_text().strip()
            priceE=pricet.get_text().strip()
        nicknameT=dataSoup.select(" span.h1_label")
        for temp in nicknameT:
            #print temp
            nickname=temp.get_text()[3:]
        print name
        #addressF=dataSoup.select(" div.list-right-text ")
        #print addressF.__len__()
        addressT=dataSoup.find_all(class_="list-right-text")
        print addressT.__len__()
        developer=addressT[0].get_text().strip()
        #print developer
        address =addressT[1].get_text().strip()
        #print address
        mainUnit=addressT[2].get_text().strip().replace("\n", ",")
        #print mainUnit
        loopPT=dataSoup.find_all(class_="list-right")
        loopP=loopPT[5].get_text().strip()
        #print loopP
        propertyType=loopPT[0].get_text().strip()
       # print propertyType
        schoolT = dataSoup.select(" div.set > p ")
        if "学校：" in schoolT[1].get_text():
           school='有学校'
        #print school
        totalHouse=loopPT[18].get_text().strip()
        #print totalHouseT
        voRatio=loopPT[14].get_text().strip()
        #print voRatioT
        greenRatio=loopPT[15].get_text().strip()
        #print greenRatioT
        propertyFee=loopPT[20].get_text().strip()[:-5]
        #print propertyFee
        propertyCompany=loopPT[19].get_text().strip()
        #print propertyCompany
        print name+"*"+nickname
        f=file('E:\\hfhouse\\fangtianxia','a+')
        new_content=name+"*"+nickname+"*"+priceE+"*"+address+"*"+propertyType+"*"+loopP+"*"+developer+"*"+mainUnit+"*"+school+"*"+voRatio+"*"+greenRatio+"*"+totalHouse+"*"+propertyFee+"*"+propertyCompany+"\n"
        f.write(new_content)
        f.close()

def nextpage(url):
    url1 = url  # fang tian xia
    #url2 = "https://hf.fang.anjuke.com/loupan/?pi=baidu-cpcaf-hf-tyonghf1&utm_source=baidu&utm_medium=cpc&kwid=40307903159&utm_term=%E6%88%BF%E6%BA%90%E7%BD%91"  # an ke ju
    # response = urllib2.urlopen(url2)
    # print response.read()
    wbdata = requests.get(url1)
    #wbdata.encoding = "gb2312"
    wbdata = wbdata.text
    # html=response.read()
    soup = BeautifulSoup(wbdata, 'lxml')
    # print soup.head
    # print soup.prettify()
    news = soup.select(" span.housetitle > a")

    for n in news:
        #print n
        print 'http://fangjia.fang.com'+str(n.get('href'))
        print n.get_text()
        if 'newhouseText' in str(n):
            print str(n.get_text())[:-7]


    '''
    for n in news:
        try:
            getdata(n.get("href"), n.get_text().strip())
        except Exception:
            f = file('E:\\hfhouse\\excep', 'a+')
            f.write(n.get("href")+"\n")
            f.close()

        # print n.get("href")
        # print n.get_text().strip()
 '''

i=1
while i<2:
    url="http://fangjia.fang.com/pghouse-c0hf/h315-i3"+str(i)+"/"
    print url
    nextpage(url)
    i=i+1



