# -*- coding: utf-8 -*
import requests
from bs4 import BeautifulSoup
import sys

reload(sys)
sys.setdefaultencoding('utf8')

def getdata(url,name):
    #print url+name
    name=name#楼盘
    #nickname=name#别名
    priceE="待定"#价格
    address=""#地址
    propertyType=""#物业类别
    #loopP=""#环线位置
    area=""#区域位置
    developer=""#开发商
    mainUnit=""#主力户型
    school=""
    voRatio=""#容积率
    greenRatio=""#绿化率
    totalHouse=""#总户数
    propertyFee=""#物业费
    propertyCompany=""
    #print name
    wbdata1 = requests.get(url)
    #wbdata1.encoding = "gb2312"
    wbdata1 = wbdata1.text
    soup1 = BeautifulSoup(wbdata1, 'lxml')
    more=soup1.select(" div.details_info > div.details_info_r > div.info_mation > ul > li > span.red24px ")
    priceE=more[0].get_text()
    #print priceE
    more1=soup1.select(" div.details_info > div.details_info_r > div.info_mation > ul > li > span.dgray14px3")
    address=more1[0].get_text()
    #print address
    more2 = soup1.select(" div.details_info > div.details_info_r > div.info_mation > ul > li > nobr > span.dgray14px3")
    mainUnit=more2[0].get_text()
    #print mainUnit

    wbdata2 = requests.get(url+"gaikuang.html")
    print url+"gaikuang.html"
    #print more[1].get("href")
    #wbdata2.encoding = "gb2312"
    wbdata2 = wbdata2.text
    #print wbdata2
    dataSoup = BeautifulSoup(wbdata2, 'lxml')
    allt=dataSoup.select('div.leftbar > table.leftbar_table > tr > td ')
    #print allt.__len__()
    #31有学校，30没学校
    if allt.__len__()==30:
        #print "noschool"
        developer = allt[5].get_text()
        propertyType = allt[8].get_text()
        #print developer+propertyType
        area = allt[10].get_text()
        voRatio = allt[13].get_text()[:-7]
        greenRatio = allt[14].get_text()[:-7]
        totalHouse = allt[17].get_text()
        propertyFee = allt[22].get_text()
        propertyCompany = allt[21].get_text()

    elif allt.__len__()==31:
        #print "school"
        developer = allt[5].get_text()
        propertyType=allt[8].get_text()
        #print developer + '*'+propertyType
        school='是'
        area=allt[11].get_text()
        voRatio = allt[14].get_text()[:-7]
        greenRatio = allt[15].get_text()[:-7]
        totalHouse = allt[18].get_text()
        propertyFee = allt[23].get_text()
        propertyCompany = allt[22].get_text()


    f = file('E:\\hfhouse\\hefangwang', 'a+')
    new_content=name+'*'+priceE+'*'+address+'*'+propertyType+'*'+area+'*'+developer+'*'+mainUnit+'*'+school+'*'+voRatio+'*'+greenRatio+'*'+totalHouse+'*'+propertyFee+'*'+propertyCompany+'\n'
    print new_content
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
    news = soup.select(" div.wrap > div.wrap900 > ul > li > div.loupan_list_info > div.loupan_tit > h3 > a ")
    for n in news:
        #print "http://newhouse.hfhouse.com"+n.get("href")
        try:
            #print n
            getdata("http://newhouse.hfhouse.com"+n.get("href"), n.get_text().strip())
        except Exception:
            print "alert this"+n.get_text().strip()+n.get("href")+"--------------------------------------------------------------------"
            f = file('E:\\hfhouse\\excep-hefangwang', 'a+')
            f.write(n.get("href")+"\n")
            f.close()

i=411
while i<413:
    url="http://newhouse.hfhouse.com/loupan//?page="+str(i)
    print url
    nextpage(url)
    i=i+1