# -*- coding: utf-8 -*
# 满意度
import urllib2
from bs4 import BeautifulSoup
import sys
import time
import json
reload(sys)
sys.setdefaultencoding("utf-8")


def getmanyi(url):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    hf = response.read()
    print hf
    soup=BeautifulSoup(hf,'lxml')
    main=soup.findAll(class_="cnt_table")
    for mm in main:
        temp=str(mm)
        soup1=BeautifulSoup(temp,'lxml')
        lines = soup1.select(" tr > td ")
        print lines.__len__()
        if lines.__len__()%6==0:
            j=0
            new_n=''
            while j < lines.__len__():
                new_n=new_n+str(lines[j].get_text().replace("\n",''))+"*"+\
                      str(lines[j+1].get_text().replace("\n",''))+"*"+\
                      str(lines[j+2].get_text().replace("\n",''))+"*"+\
                      str(lines[j+3].get_text().replace("\n",'')) +"*"+\
                      str(lines[j+4].get_text().replace("\n",''))+'\n'
                j = j + 6
            file1=file("E:\\school\\yangguanggaokao\\manyidu\\manyidu",'a+')
            file1.write(new_n)
            file1.close()





if __name__=='__main__':
    i=720
    while i<2361:
        print i
        url='http://gaokao.chsi.com.cn/zyk/pub/myd/schAppraisalTop.action?start='+str(i)
        getmanyi(url)
        i+=20
        time.sleep(2)
