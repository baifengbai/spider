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
    wbdata1 = requests.get(url)
    #wbdata1.encoding = "gb2312"
    wbdata1 = wbdata1.text
    soup1 = BeautifulSoup(wbdata1, 'lxml')
    more=soup1.select(" div.lp-navtabs-warp > div.lp-nav > ul.lp-navtabs > li > a ")
    #print more[1]
    wbdata2 = requests.get(more[1].get("href"))
    print more[1].get("href")
    #wbdata2.encoding = "gb2312"
    wbdata2 = wbdata2.text
    #print wbdata2
    dataSoup = BeautifulSoup(wbdata2, 'lxml')
    #priceT=dataSoup.select(" div.can-item > div.can-border > ul.list > li > div.des > span.can-spe")
    #print priceT[0]
    #priceE=priceT[0].get_text().strip()
    #print priceE
    #addressT=dataSoup.select(" div.can-item > div.can-border > ul.list > li > div.des")
    #print addressT[7]
    #address=addressT[7].get_text().strip()
    #if "查看地图" in address:
        #address=address[:-6].strip()
    #print address
    #propertyTyp=addressT[4].get_text().strip()
    #print propertyTyp
    #area=addressT[6].get_text().strip().replace(' ', '').replace("\n","")
    #print area
    #developer =addressT[5].get_text().strip()
    #print developer
    #print addressT[11].get_text()
    smark=dataSoup.select('ul.list > li')
    for qq in smark:
        if '楼盘地址' in str(qq):
            address =qq.get_text().strip().replace(' ', '').replace("\n","")[4:-6]
        if '物业类型' in str(qq):
            propertyType =qq.get_text().strip().replace(' ', '').replace("\n","")[4:]
        if '区域位置' in str(qq):
            area =qq.get_text().strip().replace(' ', '').replace("\n","")[4:]
        if '开发商' in str(qq):
            developer =qq.get_text().strip().replace(' ', '').replace("\n","")
        if '楼盘户型' in str(qq):
            mainUnit =qq.get_text().strip().replace(' ', '').replace("\n","")[4:-6]
        if '容积率' in str(qq):
            voRatio =qq.get_text().strip().replace(' ', '').replace("\n","")[3:-6]
        if '绿化率' in str(qq):
            greenRatio =qq.get_text().strip().replace(' ', '').replace("\n","")[3:-6]
        if '规划户数' in str(qq):
            totalHouse =qq.get_text().strip().replace(' ', '').replace("\n","")[4:-6]
        if '物业管理费' in str(qq):
            propertyFee=qq.get_text().strip().replace(' ', '').replace("\n","")[5:]
        if '物业公司' in str(qq):
            propertyCompany =qq.get_text().strip().replace(' ', '').replace("\n","")[4:]
        if '参考单价' in str(qq):
            priceE=qq.get_text().strip().replace(' ', '').replace("\n","")[4:-6]
    schoolT=dataSoup.select(" div.can-item > div.can-head > h4")
    for schh in schoolT:
        if "附近学校" in schh:
            school="是"
    f = file('E:\\hfhouse\\anjuke', 'a+')
    new_content=name+'*'+priceE+'*'+address+'*'+propertyType+'*'+area+'*'+developer+'*'+mainUnit+'*'+school+'*'+voRatio+'*'+greenRatio+'*'+totalHouse+'*'+propertyFee+'*'+propertyCompany+'\n'
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
    news = soup.select(" div.item-mod > div.infos > div.lp-name > h3 > a.items-name")
    for n in news:
        print n.get("href")
        try:
            print n
            getdata(n.get("href"), n.get_text().strip())
        except Exception:
            print "alert this"+n.get_text().strip()+n.get("href")+"--------------------------------------------------------------------"
            f = file('E:\\hfhouse\\excep-anjuke', 'a+')
            f.write(n.get("href")+"\n")
            f.close()

i=1
while i<28:
    url="https://hf.fang.anjuke.com/loupan/all/p"+str(i)+"/"
    print url
    nextpage(url)
    i=i+1