# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def nextpage(url):
    url1=url
    wbdata = requests.get(url1)
    wbdata = wbdata.content
    soup = BeautifulSoup(wbdata, 'lxml')
    '''
    lines = soup.select("tr > td > a ")
    print lines.__len__()
    for line in lines:
        if "点击查看院校信息" in str(line):
            #print line
            #print line.get_text()
            #print line.get("href")
            t=1
    lines = soup.select("tr")
    for line in lines:
        if "点击查看院校信息" in str(line):
            #print line.get_text()
            t=1
    lines = soup.findAll("td",align="left")
    for line in lines:
        if "点击查看院校信息" in str(line):
            #print line.get_text()
            t=1
    '''
    lines = soup.select(" tr > td ")
    print lines.__len__()
    ttd=52
    while ttd+6<173:
        print lines[ttd]
        print lines[ttd+1]
        print lines[ttd+2]
        print lines[ttd+3].get_text().replace("\r\t","").replace(" ","")
        #print repr(lines[ttd+3].get_text())
        print lines[ttd+4]
        print lines[ttd+5]
        ttd=ttd+6
    #for line in lines:
        #print line
    #lines1=soup.findAll("tr",onmouseover="this.style.background='#FFFFEE'")
    #print lines1.__len__()
    #for line in lines1:
        #print line

i=1
while i<2:
    url="http://gaokao.chsi.com.cn/sch/search--ss-on,searchType-1,option-qg,start-"+str(20*i-20)+".dhtml"
    print url
    nextpage(url)
    i=i+1