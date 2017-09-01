# -*- coding: utf-8 -*
from bs4 import BeautifulSoup
import urllib
import urllib2
import cookielib
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#最简单的实例，只有url
def nologin():
    #url='https://www.baidu.com/'
    #url=
    #request=urllib2.Request()
    response=urllib2.urlopen('https://www.wmzy.com/')
    #response = urllib2.urlopen('http://www.baidu.com', timeout=10)
    #response = urllib2.urlopen('http://www.baidu.com',data, 10)
    print response.read()
    print response.getcode()
    print response.headers
    print response.url
    response.close


def nologin1():
    url='https://www.wmzy.com/api/school/score-list?sch_id=52ac2e9a747aec013fcf5307&diploma=7&province=340000000000&ty=li&_=1501232898685'
    url='https://www.baidu.com/s?wd=python'
    url='https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=python&oq=python'
    values={'wd':'python'}
    data=urllib.urlencode(values)
    headers={}
    headers['User-Agent']="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36"
    '''headers['Cookie']='guide=1; score_form_scoreBox=1; _gat=1; loginByAuthcode=''; sessionid=s:vBVFwzbQxacH5gzZxXpokpOj.dMV6wDf/T9QmF6oYx9/DYa7TW/4UWChP54zEEfNrXMY; ' \
                      'Hm_lvt_02ceb62d85182f1a72db7d703affef9c=1500014794,1500602476,1500946870; Hm_lpvt_02ceb62d85182f1a72db7d703affef9c=1501227932; _ga=GA1.2.854006408.1500014610; ' \
                      'Hm_lvt_8a2f2a00c5aff9efb919ee7af23b5366=1500014611,1500602476,1500946870; Hm_lpvt_8a2f2a00c5aff9efb919ee7af23b5366=1501227939'''''
    headers['Referer']='https://www.baidu.com/'
    request=urllib2.Request(url)
    response=urllib2.urlopen(request)
    print response.read()


def nologin2():
    url='https://www.wmzy.com/api/school/score-list?sch_id=52ac2e9a747aec013fcf5307&diploma=7&province=340000000000&ty=li&_=1501232898685'
    handler = urllib2.HTTPCookieProcessor()
    #urllib2.
    opener = urllib2.build_opener(handler)
    request = urllib2.Request(url)
    response = opener.open(request)
    print response.read()


def withlogin():
    url = 'https://www.wmzy.com/api/school?home_tool'
    url = 'https://www.wmzy.com/api/school/52ac2e9a747aec013fcf5307.html'
    url = 'https://www.wmzy.com/account/ajaxLogin?_=1501232898685'
    filename = 'cookie.txt'
    cookie = cookielib.MozillaCookieJar(filename)
    handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(handler)
    values = {}
    values['account'] = '15827109637'
    values['password'] = '123abc'
    values['forceBindeCard'] = 'false'
    data = urllib.urlencode(values)
    request = urllib2.Request(url, data)
    #print request.headers
    response = opener.open(request)
    cookie.save(ignore_discard=True, ignore_expires=True)
    hd = response.read()
    print response.url
    # print response.info()
    print hd
    print response.getcode()
    print response.headers
    for item in cookie:
        print 'Name = ' + item.name
        print 'Value = ' + item.value
    response.close()
    res = opener.open(
        'https://www.wmzy.com/api/school/score-list?sch_id=52ac2e9a747aec013fcf5307&diploma=7&province=340000000000&ty=li&_=1501232898685')
    print res.read()

def withlogin1():
    url = 'https://www.wmzy.com/api/school?home_tool'
    url = 'https://www.wmzy.com/api/school/52ac2e9a747aec013fcf5307.html'
    url = 'https://www.wmzy.com/account/ajaxLogin?_=1501232898685'
    #filename = 'cookie.txt'
    cookie = cookielib.MozillaCookieJar()
    handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(handler)
    values = {}
    values['account'] = '15827109637'
    values['password'] = '123abc'
    values['forceBindeCard'] = 'false'
    data = urllib.urlencode(values)
    request = urllib2.Request(url, data)
    #print request.headers
    response = opener.open(request)
    #cookie.save(ignore_discard=True, ignore_expires=True)
    hd = response.read()
    print response.url
    # print response.info()
    print hd
    print response.getcode()
    print response.headers
    for item in cookie:
        print 'Name = ' + item.name
        print 'Value = ' + item.value
    response.close()
    res = opener.open(
        'https://www.wmzy.com/api/school/score-list?sch_id=52ac2e9a747aec013fcf5307&diploma=7&province=340000000000&ty=li&_=1501232898685')
    print res.read()



def loadCookie():
    url= 'https://www.wmzy.com/api/school/score-list?sch_id=52ac2e9a747aec013fcf5307&diploma=7&province=340000000000&ty=li&_=1501232898685'
    cookie=cookielib.MozillaCookieJar()
    cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
    req=urllib2.Request(url)
    opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    response=opener.open(req)
    print  response.read()

if __name__=="__main__":
    #nologin()
    nologin2()
    #withlogin()
    loadCookie()
    #withlogin1()