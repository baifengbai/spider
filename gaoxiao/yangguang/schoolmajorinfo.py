# -*- coding: utf-8 -*
#得到阳光高考的数据库里的学校zhuanye
import pycurl
import certifi
import StringIO
import urllib2
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def getzhuanye(name,url):
    rurl = 'http://gaokao.chsi.com.cn' + url
    request = urllib2.Request(rurl)
    response = urllib2.urlopen(request)
    # print response.read()
    hd = response.read()
    #print hd
    #print pic
    soup = BeautifulSoup(hd, 'lxml')


def get_link(name,url):
    rurl='http://gaokao.chsi.com.cn'+url
    #print rurl
    request = urllib2.Request(rurl)
    response = urllib2.urlopen(request)
    # print response.read()
    hd = response.read()
    #print hd
    #print pic
    soup = BeautifulSoup(hd, 'lxml')
    lines=soup.select(" li > a ")
    if lines[11].get_text()=='专业介绍':
        #print lines[11].get_text()
        #print lines[11].get('href')
        getzhuanye(name,lines[11].get('href'))
    else :
        print "meizhaodao"


if __name__=='__main__':
    file1=open('E:school\\yangguanglist')
    for lines in file1:
        get_link(lines.split("*")[0],lines.split("*")[1].replace("\n",''))
