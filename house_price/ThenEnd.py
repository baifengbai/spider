# -*- coding: utf-8 -*
import sys
import string
import chardet
import requests
import time
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding("utf-8")

def findxiaoqu(url):
    wbdata=requests.get(url)
    wbdata.encoding = "gb2312"
    wbdata = wbdata.text
    # html=response.read()
    soup = BeautifulSoup(wbdata, 'lxml')
    schoolname=soup.select("div.detailsTitle > h2.h2")
    #print schoolname[0].get_text()
    xiaoquname=soup.select(" p.tex > a ")
    #for xx in xiaoquname:
        #print xx.get_text()
    xoapquprice=soup.select("td > strong.num")
    #for xy in xoapquprice:
        #print xy.get_text()
    file1=open("E:\\hfhouse\\0712\\"+schoolname[0].get_text(),"a+")
    j=0
    if xiaoquname.__len__()==xoapquprice.__len__():
        while j<xiaoquname.__len__():
            new_count=xiaoquname[j].get_text()+"*"+xoapquprice[j].get_text()+"\n"
            file1.write(new_count)
            j=j+1
    else:
        print url+"----------------------"
    file1.close()
    nextpage=soup.select("a.btn_num")
    #print nextpage.__len__()
    if nextpage.__len__()>1:
        if "下一页" in nextpage[nextpage.__len__()-1].get_text():
            #print nextpage[nextpage.__len__()-1].text
            page = nextpage[nextpage.__len__()-1].get("href")
            #print page
            findxiaoqu(page)
    '''
    for nextpages in nextpage:
        
        if "下一页" in nextpages.get_text():
            print nextpages.text
            page = nextpage[0].get("href")
            print page
            findxiaoqu(page)
'''


def getschool(url):
    wbdata=requests.get(url)
    wbdata.encoding = "gb2312"
    wbdata = wbdata.text
    # html=response.read()
    soup = BeautifulSoup(wbdata, 'lxml')
    #schoolname=soup.select("a.schooltitle")
    #for names in schoolname:
        #name=names.get_text()
    url2=soup.select("dd.infodd > a.xqtxt")
    #print url2.__len__()
    for urls in url2:
        if "划片小区" in urls.text:
            urlt = urls.get("href")
            print urlt
            print "q"
            try:
                time.sleep(1)
                findxiaoqu(urlt)
            except Exception:
                print urlt+"-------------------------"



i=1
while i<35:
    url="http://hf.sell.house365.com/school/sl_p"+str(i)+".html"
    getschool(url)
    i=i+1


