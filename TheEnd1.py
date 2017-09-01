# -*- coding: utf-8 -*
import sys
import string
import chardet
import requests
import time
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding("utf-8")

def getschool(url):
    wbdata = requests.get(url)
    wbdata.encoding = "gb2312"
    wbdata = wbdata.text
    # html=response.read()
    soup = BeautifulSoup(wbdata, 'lxml')
    schoolname=soup.select("a.schooltitle")
    for names in schoolname:
        name=names.get_text()
        print name
        file1=open('C:\\Users\\Administrator\\Desktop\\365.txt')
        for lines in file1:
            #print lines.replace("\n",'')
            if name==lines.replace("\n",'').split("\t")[0]:
                print lines
                file2=open('C:\\Users\\Administrator\\Desktop\\3651.txt','a+')
                file2.write(lines)
                file2.close()



i = 1
while i < 22:
    time.sleep(1)
    url = "http://hf.sell.house365.com/school/sl_c2-p" + str(i) + ".html"
    getschool(url)
    i = i + 1


