# -*- coding: utf-8 -*
import sys
import string
import chardet
import requests
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding("utf-8")

def bab(url):
    #url = "http://www.50xiao.com/hefei/xx_zd/index_2.html"
    wbdata = requests.get(url).content
    # print wbdata
    # print chardet.detect(wbdata.text.encode('utf-8'))
    data = BeautifulSoup(wbdata, 'lxml')
    # print data
    lines = data.select(" table >  tr")
    print lines.__len__()
    file1=open("E:\\hfschool\\zhongdianmid",'a+')
    for dd in lines:
        texx = dd.text.strip().replace("\r\n", '').replace("\n\n", '').replace(
            " ", '')
        name = texx.split("评分：")[0]
        score = texx.split("评分：")[1]
        new_c=name+"*"+score+"\n"
        file1.write(new_c)
    file1.close()






i=2
while i<15:
    url="http://www.50xiao.com/hefei/xx_zd/index.html"
    url = "http://www.50xiao.com/hefei/zhongxue/index_"+str(i)+".html"
    print url
    bab(url)
    i=i+1