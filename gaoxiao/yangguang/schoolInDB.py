# -*- coding: utf-8 -*
#得到阳光高考的数据库里的v学校名单
import pycurl
import certifi
import StringIO
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf8')
i=0
while i<2641:
    url="http://gaokao.chsi.com.cn/sch/search--ss-on,searchType-1,option-qg,start-"+str(i)+".dhtml"
    c = pycurl.Curl()
    c.setopt(pycurl.CAINFO, certifi.where())
    c.setopt(c.URL, url)
    b = StringIO.StringIO()
    c.setopt(pycurl.WRITEFUNCTION, b.write)
    c.perform()
    pic = b.getvalue()
    #print pic
    soup = BeautifulSoup(pic, 'lxml')
    lines=soup.select(" tr > td > a")
    print lines.__len__()
    file1 = file("E:school\\yangguang", "a+")
    for line in range(36,lines.__len__()):
        print lines[line].get_text()
        file1.write(lines[line].get_text()+"\n")
    i=i+20
    file1.close()



