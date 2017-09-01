# -*- coding: utf-8 -*
# 章程
from bs4 import BeautifulSoup
import urllib
import urllib2
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def getzcinfo(flag,name,t1,url):
    url='http://gaokao.chsi.com.cn'+url
    request=urllib2.Request(url)
    response=urllib2.urlopen(request)
    hd =response.read()
    soup=BeautifulSoup(hd,'lxml')
    lines= soup.findAll(style='clear:both; padding:0 20px 20px 20px;')
    print lines.__len__()
    if lines.__len__()==1:
        if flag:
            path = "E:\\school\\zhangcheng\\1\\"+str(name)  # 无2017最新
        else:
            path = 'E:\\school\\zhangcheng\\2\\'+str(name)  # 有2017最新
        ipath = unicode(path, 'utf-8')
        print path
        file1 = file(ipath, 'a+')
        file1.write(str(t1)+"#$%"+str(lines[0])+"&*%")
        file1.close()

def getzhangcheng(name,url):

    url='http://gaokao.chsi.com.cn'+url
    request=urllib2.Request(url)
    response=urllib2.urlopen(request)
    hd =response.read()
    soup=BeautifulSoup(hd,'lxml')
    lines1=soup.select(" div.noInfoTxt ")
    flag=False
    for line1 in lines1:
        texte=line1.get_text()
        if '暂无2017年招生章程' in texte:
            flag=True
    lines2=soup.select(' td > a ')
    for line2 in lines2:
        try:
            getzcinfo(flag,name,line2.get_text(),line2.get('href'))
        except Exception:
            file567=file("E:\\school\\zhangcheng\\ex2",'a+')
            new_n=str(name)+str(line2.get_text())+str(line2.get('href'))
            file567.write(new_n+'\n')
            file567.close()

def getxuex(url):
    print url
    request=urllib2.Request(url)
    response=urllib2.urlopen(request)
    hd =response.read()#很奇怪，必须要有这一行为，beautifulsoup才有效，否则什么都找不到！！！
    soup=BeautifulSoup(hd,'lxml')
    lines=soup.select(" td.yes > a ")
    print lines.__len__()
    for line in lines:
        time.sleep(1)
        name=line.get_text().replace("\n",'').replace(" ",'')
        print name
        print line.get('href')
        try:
            getzhangcheng(name,line.get('href'))
        except Exception:
            file678=file("E:\\school\\zhangcheng\\ex1",'a+')
            new_n=str(name)+str(line.get('href'))
            file678.write(new_n+'\n')
            file678.close()

if __name__=='__main__':
    i=100
    while i<2701:
        print "i"
        print i
        url='http://gaokao.chsi.com.cn/zsgs/zhangcheng/listVerifedZszc--method-index,lb-1,start-'+str(i)+'.dhtml'
        getxuex(url)
        i+=100