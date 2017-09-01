# -*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import time
import urllib
import urllib2
from bs4 import BeautifulSoup
import re
import random

def getIP():
    User_Agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
    header = {}
    header['User-Agent'] = User_Agent

    url = 'http://www.66ip.cn/nmtq.php?getnum=10&isp=0&anonymoustype=0&start=&ports=&export=&ipaddress=&area=1&proxytype=0&api=66ip'
    req = urllib2.Request(url, headers=header)
    res = urllib2.urlopen(req).read()
    # print res
    lll = str(res).split("<br />")
    print lll.__len__()
    list=[]
    # print repr(lll[1].replace("\n\t\t",""))
    for i in range(1, 10):
        ipp = lll[i].replace("\r\n\t\t", "")
        print ipp
        proxy = {"http": "http://" + ipp}
        try:
            import socket
            socket.setdefaulttimeout(3)
            url1 = "http://ip.chinaz.com/getip.aspx"
            res = urllib.urlopen(url1, proxies=proxy).read()
            print res
            str1 = "{ip:'" + ipp[:-6]
            print str1
            if str1 in str(res):
                print "success"
                list.append(ipp)
        except Exception, e:
            print proxy
            print e
            continue
    return list





def getwenz(name,url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36",
        "Referer": "http://weixin.sogou.com/weixin?type=2&ie=utf8&query=%E6%9C%BA%E5%99%A8%E4%B9%8B%E5%BF%83&tsn=0&ft=&et=&interation=&wxid=oIWsFtyH4wzDYSYFwlcMk8znCtfw&usip=almosthuman2014"}
    #url = "http://weixin.sogou.com/weixin?type=2&ie=utf8&query=%E6%9C%BA%E5%99%A8%E4%B9%8B%E5%BF%83&tsn=5&ft=" + ft + "&et=" + et + "&interation=&wxid=oIWsFtyH4wzDYSYFwlcMk8znCtfw&usip=almosthuman2014"
    request = urllib2.Request(url, data, headers)
    response = urllib2.urlopen(request)
    wbdata = response.read()
    #getartical(wbdata)
    ipath = "E:\\weix\\almosthuman2014\\"+re.sub('[\/:*?"<>|]','-',name)
    file1=file(ipath,"a+")
    file1.write(wbdata)
    file1.close()


def getnextpage(url):
    url="http://weixin.sogou.com/weixin?"+url
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36",
        "Referer": "http://weixin.sogou.com/weixin?type=2&ie=utf8&query=%E6%9C%BA%E5%99%A8%E4%B9%8B%E5%BF%83&tsn=0&ft=&et=&interation=&wxid=oIWsFtyH4wzDYSYFwlcMk8znCtfw&usip=almosthuman2014",
        "Cookie":"SUV=006D7A58DCF8F32A594A6C13FDBB9728; CXID=4FC84E74769AE414650567E1E02BF2DF; ad=4kllllllll2BUAwhlllllVOo22UlllllT5083kllllwlllllROxlw@@@@@@@@@@@; SUID=2AF3F8DC3565860A59522232000C162B; ABTEST=0|1500360316|v1; IPLOC=CN3401; weixinIndexVisited=1; SNUID=F2FDAD8EAAAEFE3A776BEE47AB8185F8; JSESSIONID=aaa6RXYZEqX_I8hi-nPZv; sct=6"}
    #url = "http://weixin.sogou.com/weixin?type=2&ie=utf8&query=%E6%9C%BA%E5%99%A8%E4%B9%8B%E5%BF%83&tsn=5&ft=" + ft + "&et=" + et + "&interation=&wxid=oIWsFtyH4wzDYSYFwlcMk8znCtfw&usip=almosthuman2014"
    request = urllib2.Request(url, data, headers)
    response = urllib2.urlopen(request)
    wbdata = response.read()
    getartical(wbdata)


def getartical(wbdata):
    soup = BeautifulSoup(wbdata, 'lxml')
    links=soup.select(" div.txt-box > h3 > a")
    for link in links:
        print link.get_text()+link.get("href")
        time.sleep(0.5)
        getwenz(link.get_text(),link.get("href"))
    nexts=soup.findAll("a",id="sogou_next")
    for nextt in nexts:
        print nextt.get("href")
        getnextpage(nextt.get("href"))



def dataform(datat):
    month=datat.split("-")[1]
    day=datat.split("-")[2]
    if(int(month)<10):
        month="0"+month
    if(int(day)<10):
        day="0"+day
    return datat.split("-")[0]+"-"+month+"-"+day

def getdetail(at_1,at_2,at_3,at_4,at_5,at_6):
    user_agents = [
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60'
        'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50'
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50'
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0'
        'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10'
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2'
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16'
        'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36'
    ]
    time.sleep(0.4)
    ft_y = at_1
    ft_m = at_2
    ft_d = at_3
    et_y = at_4
    et_m = at_5
    et_d = at_6
    ft = str(ft_y) + "-" + str(ft_m) + "-" + str(ft_d)
    et = str(et_y) + "-" + str(et_m) + "-" + str(et_d)
    #print ft
    ft = dataform(ft)
    print ft
    et = dataform(et)
    print et
    headers = {
        "User-Agent": random.choice(user_agents),
        "Referer": "http://weixin.sogou.com/weixin?type=2&ie=utf8&query=%E6%9C%BA%E5%99%A8%E4%B9%8B%E5%BF%83&tsn=0&ft=&et=&interation=&wxid=oIWsFtyH4wzDYSYFwlcMk8znCtfw&usip=almosthuman2014",
        "Cookie":"SUV=006D7A58DCF8F32A594A6C13FDBB9728; CXID=4FC84E74769AE414650567E1E02BF2DF; ad=4kllllllll2BUAwhlllllVOo22UlllllT5083kllllwlllllROxlw@@@@@@@@@@@; SUID=2AF3F8DC3565860A59522232000C162B; ABTEST=0|1500360316|v1; IPLOC=CN3401; weixinIndexVisited=1; SNUID=F2FDAD8EAAAEFE3A776BEE47AB8185F8; JSESSIONID=aaa6RXYZEqX_I8hi-nPZv; sct=6"}
    url = "http://weixin.sogou.com/weixin?type=2&ie=utf8&query=%E6%9C%BA%E5%99%A8%E4%B9%8B%E5%BF%83&tsn=5&ft=" + ft + "&et=" + et + "&interation=&wxid=oIWsFtyH4wzDYSYFwlcMk8znCtfw&usip=almosthuman2014"
    request = urllib2.Request(url, data, headers)

    response = urllib2.urlopen(request)
    wbdata = response.read()
    #print wbdata
    print "xx"
    if "sogou_page_10" in wbdata:
        print "超过10页"
        if (et_y - ft_y) == 2:
            et_y=et_y-1
            getdetail(ft_y, ft_m, ft_d, et_y, et_m, et_d)
        elif (et_y - ft_y) == 1:
            et_m=(ft_m+12+et_m)/2
            if et_m>12:
                et_m=et_m-12
                getdetail(ft_y, ft_m, ft_d, et_y, et_m, et_d)
            else:
                et_y=ft_y
                getdetail(ft_y, ft_m, ft_d, et_y, et_m, et_d)
        elif et_y ==ft_y:

            if (et_m-ft_m)>1:
                et_m = (ft_m + et_m) / 2
                getdetail(ft_y, ft_m, ft_d, et_y, et_m, et_d)
            elif (et_m-ft_m)==1:
                et_d=(ft_d+et_d+28)/2
                if et_d>28:
                    et_d=et_d-28
                    getdetail(ft_y, ft_m, ft_d, et_y, et_m, et_d)
                else:
                    et_m=ft_m
                    getdetail(ft_y, ft_m, ft_d, et_y, et_m, et_d)
            else:
                if et_d==ft_d:
                    #getartical(wbdata)
                    print "artical too much"
                else:
                    et_d = (et_d + ft_d) / 2
                    getdetail(ft_y, ft_m, ft_d, et_y, et_m, et_d)
        else:
            et_y=(et_y+ft_y)/2
            getdetail(ft_y, ft_m, ft_d, et_y, et_m, et_d)
    elif "用户您好，您的访问过于频繁，为确认本次访问为正常用户行为，需要您协助验证" in wbdata:
        print "哈哈，要输入验证码"
        #换IP，重新搞！！
        ip_list=getIP()
        while ip_list.__len__()<1:
            time.sleep(10)
            ip_list=getIP()

        proxy_support = urllib2.ProxyHandler({'http': ip_list[0]})
        opener = urllib2.build_opener(proxy_support)
        urllib2.install_opener(opener)
        request = urllib2.Request(url, data, headers)

    else:
        print "小雨10页了"
        #getartical(wbdata)
        if et_y==2017 and et_m==7 and et_d==18:
            print "OK"
        else:
            ft_y=et_y
            ft_m=et_m
            ft_d=et_d+1
            et_y=2017
            et_m=7
            et_d=18
            getdetail(ft_y, ft_m, ft_d, et_y, et_m, et_d)


values={}
data = urllib.urlencode(values)
ft_y=2014
ft_m=07
ft_d=19
et_y=2017
et_m=07
et_d=18
getdetail(ft_y,ft_m,ft_d,et_y,et_m,et_d)
#ft="2011-01-12"
#et="2017-07-18"


