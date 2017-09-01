# -*- coding: utf-8 -*
import requests
from bs4 import BeautifulSoup
import sys
import time
reload(sys)
sys.setdefaultencoding('utf8')

def getdata(url,name,map,pricee):
    #print url+name
    name=name#楼盘
    priceE=pricee#价格
    address=""#地址
    propertyType=""#物业类别
    #area=""#区域位置
    developer=""#开发商
    mainUnit=""#主力户型
    school=""
    voRatio=""#容积率
    greenRatio=""#绿化率
    #totalHouse=""#总户数
    propertyFee=""#物业费
    propertyCompany=""
    mapP=map#经纬度
    #print name
    wbdata1 = requests.get(url)
    #wbdata1.encoding = "gb2312"
    wbdata1 = wbdata1.text
    soup1 = BeautifulSoup(wbdata1, 'lxml')
    more=soup1.select(" div.detailed-information > dl.clearfix > dd ")

    #moret=soup1.select(" div.detailed-information")
    #print moret.__len__()
    if more.__len__()==28:
        #print more.__len__()
        address=more[5].get_text().strip()[:-2]
        propertyType=more[1].get_text().strip()
        developer=more[7].get_text().strip()
        school=more[19].get_text().strip()
        voRatio=more[15].get_text().strip()
        greenRatio=more[16].get_text().strip()
        propertyFee=more[18].get_text().strip()
        propertyCompany=more[17].get_text().strip()
    elif more.__len__()==34 or more.__len__()==41:
        #print more.__len__()
        address=more[5].get_text().strip()[:-2]
        propertyType=more[1].get_text().strip()
        developer=more[7].get_text().strip()
        mainUnit = more[11].get_text().strip()
        school=more[25].get_text().strip()
        voRatio=more[21].get_text().strip()
        greenRatio=more[22].get_text().strip()
        propertyFee=more[24].get_text().strip()
        propertyCompany=more[23].get_text().strip()
    new_content=name+'*'+priceE+'*'+address+'*'+propertyType+'*'+developer+'*'+str(mainUnit).replace("\r\n",'').replace(" ",'').rstrip()+'*'+school+'*'+voRatio+'*'+greenRatio+'*'+propertyFee+'*'+propertyCompany+'*'+map+'\n'
    print new_content
    print repr(more[11].get_text())
    f = file('E:\\hfhouse\\xafc', 'a+')
    #new_content=name+'*'+priceE+'*'+address+'*'+propertyType+'*'+developer+'*'+mainUnit+'*'+school+'*'+voRatio+'*'+greenRatio+'*'+propertyFee+'*'+propertyCompany+'*'+map+'\n'
    #print new_content
    f.write(new_content)
    f.close()

def nextpage(url):
    url1 = url  # fang tian xia
    wbdata = requests.get(url1)
    #wbdata.encoding = "gb2312"
    wbdata = wbdata.text
    # html=response.read()
    soup = BeautifulSoup(wbdata, 'lxml')
    # print soup.head
    # print soup.prettify()
    news = soup.find_all(class_="item-mod srollmap")
    #print news.__len__()
    ''''''
    for n in news:
        time.sleep(1)
        #print "http://newhouse.hfhouse.com"+n.get("href")
        try:
            print n.get("housename")+'*'+n.get('data-link')+'*'+n.get('housemap')+'*'+n.get('houseprice')
            getdata(n.get('data-link')+'xinxi.html', n.get("housename"),n.get('housemap'),n.get('houseprice'))
        except Exception:
            print "alert this"+n.get('data-link')+'xinxi.html'+"--------------------------------------------------------------------"
            f = file('E:\\hfhouse\\excep-xafc', 'a+')
            f.write(n.get('data-link')+'xinxi.html'+"\n")
            f.close()

i=1
while i<159:
    url="http://house.xafc.com/list.html?kw=&page="+str(i)
    print url
    nextpage(url)
    i=i+1