# -*- coding: utf-8 -*
#得到阳光高考的学校名单
import pycurl
import certifi
import StringIO
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf8')
i=22
while i<33:
    url="http://gaokao.chsi.com.cn/gkxx/zszcgd/dnzszc/201706/20170615/1611254988-"+str(i)+".html"
    c = pycurl.Curl()
    c.setopt(pycurl.CAINFO, certifi.where())
    c.setopt(c.URL, url)
    b = StringIO.StringIO()
    c.setopt(pycurl.WRITEFUNCTION, b.write)
    c.perform()
    pic = b.getvalue()
    #print pic

    soup = BeautifulSoup(pic, 'lxml')
    lines=soup.select(" tr > td")
    print lines.__len__()
    i=i+1
    j=1
    file1=file("E:\\school\\schoollist\\schoollist1",'a+')
    while j<lines.__len__()-1:
        line=lines[j].get_text().replace("\r\n\t",'')+"*"+lines[j+1].get_text().replace("\r\n\t",'')+"*"+lines[j+2].get_text().replace("\r\n\t",'')+"*"+lines[j+3].get_text().replace("\r\n\t",'')+"*"+lines[j+4].get_text().replace("\r\n\t",'')+"*"+lines[j+5].get_text().replace("\r\n\t",'')+"*"+lines[j+6].get_text().replace("\r\n\t",'')+'\n'
        file1.write(line)
        print repr(line)
        j=j+7
    file1.close()



