# -*- coding: utf-8 -*
#高考派的各省市批次线
import pycurl
import StringIO
import certifi
import time
import sys
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf8')


def getgrade(url):
    #url="http://www.gaokaopai.com/fenshuxian-sct-3-p-2.html"
    c = pycurl.Curl()
    c.setopt(pycurl.CAINFO, certifi.where())
    c.setopt(c.URL, url)
    b = StringIO.StringIO()
    c.setopt(pycurl.WRITEFUNCTION, b.write)
    c.perform()
    wbdata = b.getvalue()
    #print wbdata
    soup=BeautifulSoup(wbdata,'lxml')
    lines=soup.select(" tr > td ")
    print lines.__len__()
    j=1
    while j<lines.__len__()-2:
        new_count=lines[j].get_text()+"*"+lines[j+1].get_text()+"*"+lines[j+2].get_text()+"*"+lines[j+3].get_text()+"*"+lines[j+4].get_text().replace("\r\n","").replace(" ",'')+"\n"
        #print repr(lines[j+4].get_text())
        print new_count
        file1 = file("E:\\school\\schoolprovince\\gaokaopaigrade", 'a+')
        file1.write(new_count)
        file1.close()
        j=j+5


if __name__=='__main__':
    i=1
    while i<17:
        time.sleep(0.4)
        url="http://www.gaokaopai.com/fenshuxian-sct-3-year-2012-p-"+str(i)+".html"
        getgrade(url)
        i=i+1