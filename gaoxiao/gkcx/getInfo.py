# -*- coding: utf-8 -*
# 得到高考教育在线的大学info
# 得到院校详细信息，包括。。。。
import time
import pycurl
import certifi
import StringIO
import json
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf8')


file1=open("E:\\school\\schoolid1")
for lines in file1:
    time.sleep(1)
    id=lines.split("*")[5]
    print lines.split("*")[0]
    url = "http://gkcx.eol.cn/schoolhtm/schoolTemple/school"+id+".htm"#主页
    url1="http://gkcx.eol.cn/schoolhtm/schoolInfo/"+id+"/10056/detail.htm"#简介
    url2="http://gkcx.eol.cn/schoolhtm/specialty/specialtyList/specialty"+id+".htm"#专业
    url3="http://gkcx.eol.cn/schoolhtm/schoolInfo/"+id+"/10071/list_1.htm"#招生章程
    c = pycurl.Curl()
    c.setopt(pycurl.CAINFO, certifi.where())
    c.setopt(c.URL, url1)
    b = StringIO.StringIO()
    c.setopt(pycurl.WRITEFUNCTION, b.write)
    c.perform()
    pic = b.getvalue()
    soup=BeautifulSoup(pic,'lxml')
    brief=soup.find(class_="content news")
    #print brief.text
    linee=soup.select(" li > div > span ")
    #print linee[0].get_text()
    #print linee[1].get_text()
    #print linee[2].get_text()
    path="E:\\school\\schoolinfo\\"+lines.split("*")[0]
    path1 = unicode(path, 'utf-8')
    file2=file(path1,'a+')
    xxx=""
    if "曾用名：" in lines.split("*")[14]:
        xxx=lines.split("*")[14].split("曾用名：")[1]
    new_count=""
    try:
        new_count=lines.split("*")[0]+"&%*"+lines.split("*")[1]+"&%*"+lines.split("*")[2]+"&%*"+lines.split("*")[3]+"&%*"+lines.split("*")[4]+"&%*"+lines.split("*")[5]+"&%*"+lines.split("*")[6]+"&%*"+lines.split("*")[7]+"&%*"+lines.split("*")[8]+"&%*"+lines.split("*")[9]+"&%*"+lines.split("*")[10]+"&%*"+lines.split("*")[11]+"&%*"+lines.split("*")[12]+"&%*"+lines.split("*")[13]+"&%*"+xxx+"&%*"+linee[0].get_text()+"&%*"+linee[1].get_text()+"&%*"+linee[2].get_text()+"&%*"+brief.text
    except Exception:
        urlttt = "http://gkcx.eol.cn/schoolhtm/schoolTemple/school" + id + ".htm"  # 主页
        c1 = pycurl.Curl()
        c1.setopt(pycurl.CAINFO, certifi.where())
        c1.setopt(c1.URL, urlttt)
        b1 = StringIO.StringIO()
        c1.setopt(pycurl.WRITEFUNCTION, b1.write)
        c1.perform()
        pic = b1.getvalue()
        soup = BeautifulSoup(pic, 'lxml')
        brief = soup.find(class_="content news")
        # print brief.text
        linee = soup.select(" li > div > span ")
        new_count=lines.split("*")[0]+"&%*"+lines.split("*")[1]+"&%*"+lines.split("*")[2]+"&%*"+lines.split("*")[3]+"&%*"+lines.split("*")[4]+"&%*"+lines.split("*")[5]+"&%*"+lines.split("*")[6]+"&%*"+lines.split("*")[7]+"&%*"+lines.split("*")[8]+"&%*"+lines.split("*")[9]+"&%*"+lines.split("*")[10]+"&%*"+lines.split("*")[11]+"&%*"+lines.split("*")[12]+"&%*"+lines.split("*")[13]+"&%*"+xxx+"&%*"+linee[0].get_text()+"&%*"+linee[1].get_text()+"&%*"+linee[2].get_text()+"&%*"
        c1.close()
        b1.close()


    file2.write(new_count)

    file2.close()
    b.close()
    c.close()
file1.close()




