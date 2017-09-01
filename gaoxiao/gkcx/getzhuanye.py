# -*- coding: utf-8 -*
#
import pycurl
import certifi
import StringIO
import time
from bs4 import BeautifulSoup
import sys

reload(sys)
sys.setdefaultencoding('utf8')

def getmajorinfo(url):
    c = pycurl.Curl()
    c.setopt(pycurl.CAINFO, certifi.where())
    c.setopt(c.URL, 'http://gkcx.eol.cn'+str(url))
    b = StringIO.StringIO()
    c.setopt(pycurl.WRITEFUNCTION, b.write)
    c.setopt(pycurl.ACCEPTTIMEOUT_MS,30000)
    c.setopt(pycurl.HTTPPROXYTUNNEL)
    c.setopt(pycurl.TIMEOUT_MS, 30000)
    try:
        c.perform()
    except Exception:
        print '2'
        c.perform()
    pic = b.getvalue()
    b.close()
    c.close()
    soup=BeautifulSoup(pic,'lxml')
    info=soup.findAll(class_='content news')
    #print info.__len__()
    if info.__len__()==0:
        return ""
    else :
        return info[0]

def getmajorname(name,url):
    c = pycurl.Curl()
    c.setopt(pycurl.CAINFO, certifi.where())
    c.setopt(c.URL, url)
    b = StringIO.StringIO()
    c.setopt(pycurl.WRITEFUNCTION, b.write)
    c.setopt(pycurl.ACCEPTTIMEOUT_MS,35000)
    c.setopt(pycurl.TIMEOUT_MS, 35000)
    c.perform()
    pic = b.getvalue()
    b.close()
    c.close()
    soup=BeautifulSoup(pic,'lxml')
    majors=soup.select(' ul.li-major > li > a')
    print majors.__len__()
    new_n=[]
    if majors.__len__()!=0:
        for major in majors:
            print major.get_text()
            mtt=''
            try:
                mtt = getmajorinfo(major.get('href'))
            except Exception:
                print 'second'
                mtt = getmajorinfo(major.get('href'))

            info = str(major.get_text()) + '%*' + str(mtt
                )+'$&*'
            new_n.append(info)
    print new_n
    path='E:\\school\\eolmajor1\\'+name
    path1 = unicode(path, 'utf-8')
    file2 = file(path1, 'a+')
    for lines in new_n:
        file2.write(lines)
    file2.close()


def geturl(name,id):
    url='http://gkcx.eol.cn/schoolhtm/specialty/specialtyList/specialty'+str(id)+'.htm'
    getmajorname(name,url)

if __name__=='__main__':
    fil1=open('E:\\school\\schoolid-exx')
    for lines in fil1:
        print lines.split("*")[0]
        #geturl(lines.split("*")[0], lines.split("*")[5])
        try:
            geturl(lines.split("*")[0],lines.split("*")[5])
            #pass
        except Exception:
            print Exception
            file2=file('E:\\school\\schoolid-exxx','a+')
            file2.write(lines)
            file2.close()

    fil1.close()