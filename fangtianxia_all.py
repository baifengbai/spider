# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import sys

reload(sys)
sys.setdefaultencoding('utf8')


def getdata(url, name):
    name = name.replace("\n", '').strip().replace("\r\n", '')
    nickname = name
    priceE = ""
    address = ""
    propertyType = ""
    area = ""
    loopP = ""
    developer = ""
    mainUnit = ""
    school = ""
    voRatio = ""
    greenRatio = ""
    totalHouse = ""
    propertyFee = ""
    propertyCompany = ""
    wbdata1 = requests.get(url)
    wbdata1.encoding = "gb2312"
    wbdata1 = wbdata1.text
    soup = BeautifulSoup(wbdata1, 'lxml')
    lines = soup.select(" div.information_li > div.fl > p > a ")
    # print lines.__len__()
    # find_all(class_="fl more")
    lines2 = soup.select("a.more-detail")
    if lines.__len__() == 1:
        print "fl more"
        for n in lines:
            # print n
            print n.get('href')
            wbdata4 = requests.get(n.get('href'))
            wbdata4.encoding = "gb2312"
            wbdata4 = wbdata4.text
            sop1 = BeautifulSoup(wbdata4, 'lxml')
            slin0 = sop1.select(" div.main-info-price ")
            for slin0s in slin0:
                priceE = slin0s.get_text()
            if "价格：" in priceE:
                priceE = priceE.replace("价格：", '').strip().replace("\n", '')
            if "均价约" in priceE:
                priceE = priceE.replace("均价约", '')
            if "元/平方米" in priceE:
                priceE = priceE.replace("元/平方米", '')
            # print priceE
            slin1 = sop1.select(" div.lpbt > span.h1_label ")
            for slin1s in slin1:
                nickname = slin1s.get_text()
            if "别名：" in nickname:
                nickname = nickname.replace("别名：", "")
            slif = sop1.select(" div.list-right-text ")
            # print slif.__len__()
            developer = slif[0].get_text().strip().replace("\n", "").replace(" ", '')
            address = slif[1].get_text().strip().replace("\n", "").replace(" ", '')
            mainUnit = slif[2].get_text().strip().replace("\n", "").replace(" ", '')

            slin = sop1.select(" ul.list > li ")
            # print slin.__len__()
            for sli in slin:
                temp = sli.get_text().strip().replace("\n", "").replace(" ", '')
                # print temp
                if "物业类别：" in sli.get_text()[0:6]:
                    # print sli.get_text()
                    propertyType = temp.replace("物业类别：", '').replace("\t", '')
                    print propertyType
                    # print repr(propertyType)
                elif "容积率：" in sli.get_text()[0:5]:
                    # print sli.get_text()
                    voRatio = temp.replace("容积率：", '')
                    print voRatio
                elif "绿化率：" in sli.get_text()[0:5]:
                    # print sli.get_text()
                    greenRatio = temp.replace("绿化率：", '')
                    print greenRatio
                elif "总户数：" in sli.get_text()[0:5]:
                    # print sli.get_text()
                    totalHouse = temp.replace("总户数：", '')
                    print totalHouse
                elif "物业公司：" in sli.get_text()[0:6]:
                    # print sli.get_text()
                    propertyCompany = temp.replace("物业公司：", '')
                    print propertyCompany
                elif "物业费：" in sli.get_text()[0:5]:
                    # print sli.get_text()
                    propertyFee = temp.replace("物业费：", '')
                    print propertyFee
            xyz = sop1.select("li > div.list-right")
            # print xyz.__len__()
            loopP = xyz[5].get_text().strip().replace("\n", "").replace(" ", '')
            # print loopP
            # for xyzs in xyz:
            # print xyzs.get_text().strip().replace("\n","").replace(" ",'')
            sch = sop1.select(" div.set")
            print sch.__len__()
            if sch.__len__() == 2:
                if "学   区" in str(sch[1].get_text):
                    school = "是"
    elif lines2.__len__() == 1:
        print "more detail"
        for n in lines2:
            # print n.get("href")
            wbdata3 = requests.get(n.get("href"))
            wbdata3.encoding = "gb2312"
            wbdata3 = wbdata3.text
            soup1 = BeautifulSoup(wbdata3, 'lxml')
            lines3 = soup1.select("div.plptinfo_list > ul > li")
            # print lines3.__len__()
            for infodata in lines3:
                # print infodata.get_text()
                if "地址：" in infodata.get_text():
                    # print "地址："+infodata.get_text()
                    address = infodata.get_text().split("地址：")[1]
                    if "查看地图" in address:
                        address = address.replace("查看地图", '')
                        # print address
                elif "物业类型：" in infodata.get_text():
                    propertyType = infodata.get_text().split("业类型：")[1]
                    # print propertyType
                elif "开 发 商" in infodata.get_text():
                    developer = infodata.get_text().split("：")[1]
                    # print developer
                elif "周边学校" in infodata.get_text():
                    school = infodata.get_text().split("：")[1].strip().replace("\n", '')
                    # print school
                elif "容 积 率" in infodata.get_text():
                    voRatio = infodata.get_text().split("：")[1]
                    # print voRatio
                elif "绿 化 率" in infodata.get_text():
                    greenRatio = infodata.get_text().split("：")[1]
                    # print greenRatio
                elif "总 户 数" in infodata.get_text():
                    totalHouse = infodata.get_text().split("：")[1]
                    # print totalHouse
                elif "物 业 费" in infodata.get_text():
                    propertyFee = infodata.get_text().split("：")[1]
                    # print propertyFee
                elif "物业公司" in infodata.get_text():
                    propertyCompany = infodata.get_text().split("：")[1]
                    # print propertyCompany
                elif "所在区域" in infodata.get_text():
                    area = infodata.get_text().split("：")[1]
                    # print area
            lines4 = soup1.select(" div.plptinfoa > div.tdnr > div.s2 ")
            # print lines4.__len__()
            if lines4.__len__() == 1:
                for prices in lines4:
                    priceE = prices.get_text()
                    # print priceE
            line5 = soup1.select(" div.ceninfo_sq > h1 > span > span")
            for line5s in line5:
                nickname = line5s.get_text()
                if "别名：" in nickname:
                    nickname = nickname.replace("别名：", "")
                    # print nickname
                    # print n
    f = file('E:\\hfhouse\\fangtianxia_all', 'a+')
    new_content = name + "*" + nickname + "*" + priceE + "*" + address + "*" + propertyType + "*" + area + "*" + loopP + "*" + developer + "*" + mainUnit + "*" + school + "*" + voRatio + "*" + greenRatio + "*" + totalHouse + "*" + propertyFee + "*" + propertyCompany + "\n"
    # print name
    # print repr(name)
    f.write(new_content)
    f.close()


def nextpage(url):
    url1 = url
    wbdata = requests.get(url1)
    wbdata = wbdata.text
    # html=response.read()
    soup = BeautifulSoup(wbdata, 'lxml')
    lines = soup.select(" span.housetitle > a")
    i = 0
    for n in lines:
        # print n
        print 'http://fangjia.fang.com' + str(n.get('href'))

        name = n.get_text()
        if 'newhouseText' in str(n):
            name = str(n.get_text())[:-7]
        print name.strip()
        getdata('http://fangjia.fang.com' + str(n.get('href')), name)
        i = i + 1
    print i


i = 1
while i < 18:
    url = "http://fangjia.fang.com/pghouse-c0hf/h315-i3" + str(i) + "-j3140/"
    print url
    nextpage(url)
    i = i + 1
