# -*- coding: utf-8 -*
# 学汁平台
import pycurl
import certifi
import StringIO
import urllib2
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def getzhiye(name,url):
    url='http://xz.chsi.com.cn'+url
    try:
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
    except Exception:
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)

    hd = response.read()
    #print hd
    soup=BeautifulSoup(hd,'lxml')
    lines=soup.findAll(id='occ',)
    print lines.__len__()
    if lines.__len__()==1:
        for line in lines:
            # print line
            soup1 = BeautifulSoup(str(line), 'lxml')
            qqq = soup1.select(' li > a ')
            print qqq.__len__()

            new_n=name
            for content in qqq:
                new_n=new_n+"*"+content.get_text().replace("\n",'')
            file2 = file('E:\\school\\yangguanggaokao\\zhuanye_yangguang','a+')
            file2.write(new_n+"\n")
            file2.close()





def getzz(url):
    try:
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
    except Exception:
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)

    hd = response.read()
    #print hd
    soup=BeautifulSoup(hd, 'lxml')
    lines=soup.select('tr > td > a')
    print lines.__len__()
    for line in lines:
        print line.get_text()
        print line.get('href')
        try:
            getzhiye(line.get_text(), line.get('href'))
        except Exception:
            getzhiye(line.get_text(), line.get('href'))


if __name__=='__main__':
    i=0
    while i < 474:
        print "page:"+str(i)
        url='http://xz.chsi.com.cn/speciality/list.action?xk=&ml=&cc=1050&zymc=&start='+str(i)
        getzz(url)
        i+=30