# -*- coding: utf-8 -*
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import urllib
import urllib2
from bs4 import BeautifulSoup

User_Agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
header = {}
header['User-Agent'] = User_Agent

url = 'http://www.66ip.cn/nmtq.php?getnum=10&isp=0&anonymoustype=0&start=&ports=&export=&ipaddress=&area=1&proxytype=0&api=66ip'
req = urllib2.Request(url,headers=header)
res = urllib2.urlopen(req).read()
#print res
lll=str(res).split("<br />")
print lll.__len__()
list=[]
#print repr(lll[1].replace("\n\t\t",""))
for i in range(1,10):
    ipp=lll[i].replace("\r\n\t\t","")
    print ipp
    proxy={"http":"http://"+ipp}
    try:
        import socket
        socket.setdefaulttimeout(3)
        url1 = "http://ip.chinaz.com/getip.aspx"
        res = urllib.urlopen(url1,proxies=proxy).read()
        print res
        str1="{ip:'"+ipp[:-6]
        print str1
        if str1 in str(res):
            print "success"
            list.append(ipp)
    except Exception,e:
        print proxy
        print e
        continue
print "ok"+list[0]
