# -*- coding: utf-8 -*
# 作废
from bs4 import BeautifulSoup
import urllib
import urllib2
import sys
import time
from random import choice
import imp
B=imp.load_source('B','C:\\Users\\Administrator\\PycharmProjects\\spiders\\IP\\ttIP.py')
reload(sys)
sys.setdefaultencoding('utf8')

def getZZ(name,url,list):
    time.sleep(2)
    url='https://www.wmzy.com'+url
    try:
        print choice(list)
        proxy_handler = urllib2.ProxyHandler({"http": choice(list)(list,1)[1:-1]})
        opener = urllib2.build_opener(proxy_handler)
        request = urllib2.Request(url)
        response = opener.open(request)
    except Exception:
        print choice(list)
        time.sleep(10)
        proxy_handler = urllib2.ProxyHandler({"http": choice(list)})
        opener = urllib2.build_opener(proxy_handler)
        request = urllib2.Request(url)
        response = opener.open(request)
    #print response.read()
    soup=BeautifulSoup(response.read(),'lxml')
    lines=soup.select("div.m-major-product")
    print lines.__len__()
    for line in lines:
        if line.get_text().replace("\n",'').replace(" ", '')=="暂无":
            continue
        path="E:\\school\\zhuanye\\all\\"+name
        #path1 = unicode(path, 'utf-8')
        file1=file(path,'a+')
        file1.write(str(line))
        file1.close()
    response.close()


url='http://www.gaokaopai.com/zhuanye.html'
#url='http://edu.jobui.com/majors/benke/zhexue/#010100'
headers={'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36',
         'Cookie':'liyungf_tc=AQAAANlSJG7wcQoAWVcHJI5H5JbNZUWP; acw_tc=AQAAAKVI6Q9iHQsAWVcHJMAZMIfAv79C; PHPSESSID=t7hq4rmr8gbravvcjpf55q57u1; SERVERID=70bbdefa3b448ccda1465d71e2b3764b|1501567851|1501567154; Hm_lvt_c2c1aeb9dd53d590e8d4109d912eed04=1501135391,1501135933,1501136310,1501139056; Hm_lpvt_c2c1aeb9dd53d590e8d4109d912eed04=1501567849; _ga=GA1.2.375727910.1499932018; _gid=GA1.2.687151257.1501549648; td_cookie=18446744073567189061',
         'Referer':'http://www.gaokaopai.com',
         'Upgrade-Insecure-Requests':'1',
         'Host':'www.gaokaopai.com'}
request = urllib2.Request(url,headers=headers)
response = urllib2.urlopen(request)
#print response.read()
#print str(response.read())
soup=BeautifulSoup(str(response.read()),'lxml')
lines=soup.select(" li > a ")
print lines.__len__()
list=B.getIP().getIPlist()
for ll in lines:
    print ll.get_text()
'''
for line in range(476,lines.__len__()):
    print line
    print lines[line].get_text().replace("\n",'').replace(" ",'')
    #print lines[line].get('href')
    try:
        getZZ(lines[line].get_text().replace("\n",'').replace(" ",''), lines[line].get('href'),list)
    except Exception:
        file2=file("E:\\school\\zhuanye\\exxx",'a+')
        file.write(str(lines[line].get_text().replace("\n",'').replace(" ",''))+'\n')
        file2.close()
'''