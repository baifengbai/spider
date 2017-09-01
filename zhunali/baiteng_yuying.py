# -*- coding: utf-8 -*
import pycurl
import certifi
import StringIO
import time
import json
import sys
import urllib
import urllib2
import pymysql
from random import choice
from bs4 import BeautifulSoup


def get_time():
    time_now = repr(time.time()*1000)
    return time_now[:-2]


reload(sys)
sys.setdefaultencoding("utf-8")
number = 0


def getList():
    list = []
    conn = pymysql.connect(host = '172.31.8.10', port = 3306, user = 'jiezhang',
                           password = 'jiezhang', db='zhiyuan', charset = 'utf8')
    cursor = conn.cursor()
    sql = "SELECT * FROM IPproxy ORDER BY grade DESC LIMIT 0,400"
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        list.append(row[0]+":"+row[1])
    return list


def statues(IPlist, id):
    global number
    # status
    url = 'http://www.patexplorer.com/patent/view/' + id + '/legal/status?_=' + get_time()
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'
    #headers['Cookie'] = '__jsluid=b96693d21e33e599750c8b14263094d5; UM_distinctid=15d5aee2a032df-079a7a03674693-474b0421-100200-15d5aee2a04762; CNZZDATA1253901093=720767245-1500466963-null%7C1501811796; Hm_lvt_1761fabf3c988e7f04bec51acd4073f4=1500469144,1501815\
    #838; Hm_lpvt_1761fabf3c988e7f04bec51acd4073f4=1501815927; td_cookie=18446744069520568683'
    headers['Referer'] = 'http://www.patexplorer.com/results/s.html?sc=63&q=%28ad%3A%5B19480801+TO+20170808%5D%29&fq=type%3A%28cn_in%29&type=s&sort=&sortField='
    #headers["X-Forwarded-For"] = choice(IPlist)
    request = urllib2.Request(url, headers=headers)
    #request.set_proxy(choice(IPlist), 'http')
    hd = ''
    response_code = "0"
    while response_code != "200":
        try:
            number +=1
            print number
            response = urllib2.urlopen(request, timeout=2)
            response_code = str(response.getcode())
            print response_code
            if response_code == '404':
                return
            hd = response.read()
        except:
            pass
    # print hd
    soup = BeautifulSoup(hd,'lxml')
    lines = soup.select(" td ")
    file3 = file('E:\\zhuanli\\yuyin\\' + id + "_status", 'a+')
    for line in lines:
        print line.get_text()
        file3.write(line.get_text().replace("\n", ""))
        file3.write("\n")
    checking = soup.findAll(p='law-ing checking')
    for checks in checking:
        print checks
        file3.write('当前法律状态：')
        file3.write(str(checks).replace("\n"), '')
        file3.write("\n")
    file3.close()


# pdf
def pdf(IPlist, id):
    global number
    # pdf
    url = 'http://www.patexplorer.com/patent/view/'+id+'/detail/pdf?_='+get_time()
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'
    #headers['Cookie'] = '__jsluid=b96693d21e33e599750c8b14263094d5; UM_distinctid=15d5aee2a032df-079a7a03674693-474b0421-100200-15d5aee2a04762; CNZZDATA1253901093=720767245-1500466963-null%7C1501811796; Hm_lvt_1761fabf3c988e7f04bec51acd4073f4=1500469144,1501815\
    #838; Hm_lpvt_1761fabf3c988e7f04bec51acd4073f4=1501815927; td_cookie=18446744069520568683'
    headers['Referer'] = 'http://www.patexplorer.com/results/s.html?sc=63&q=%28ad%3A%5B19480801+TO+20170808%5D%29&fq=type%3A%28cn_in%29&type=s&sort=&sortField='
    #headers["X-Forwarded-For"] = choice(IPlist)
    request = urllib2.Request(url, headers=headers)
    #request.set_proxy(choice(IPlist), 'http')
    hd = ''
    response_code = "0"
    while response_code != "200":
        try:
            number +=1
            print number
            response = urllib2.urlopen(request, timeout=2)
            response_code = str(response.getcode())
            print response_code
            if response_code == '404':
                return
            hd = response.read()
        except:
            pass
    # print hd
    soup = BeautifulSoup(hd,'lxml')
    lines = soup.select(" img.lazyload ")
    file3 = file('E:\\zhuanli\\yuyin\\' + id + "_pdf", 'a+')
    for line in lines:
        print line.get("data-url")
        file3.write(line.get("data-url"))
        file3.write("\n")
    file3.close()


# 说明书
def desc(IPlist, id):
    global number
    url = 'http://www.patexplorer.com/patent/view/'+id+'/detail/desc?_='+get_time()
    # pdf
    #url = 'http://www.patexplorer.com/patent/view/'+id+'/detail/pdf?_='+get_time()
    # status
    #url = 'http://www.patexplorer.com/patent/view/'+id+'/legal/status?_='+get_time()
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'
    #headers['Cookie'] = '__jsluid=b96693d21e33e599750c8b14263094d5; UM_distinctid=15d5aee2a032df-079a7a03674693-474b0421-100200-15d5aee2a04762; CNZZDATA1253901093=720767245-1500466963-null%7C1501811796; Hm_lvt_1761fabf3c988e7f04bec51acd4073f4=1500469144,1501815\
    #838; Hm_lpvt_1761fabf3c988e7f04bec51acd4073f4=1501815927; td_cookie=18446744069520568683'
    headers['Referer'] = 'http://www.patexplorer.com/results/s.html?sc=63&q=%28ad%3A%5B19480801+TO+20170808%5D%29&fq=type%3A%28cn_in%29&type=s&sort=&sortField='
    #headers["X-Forwarded-For"] = choice(IPlist)
    request = urllib2.Request(url, headers=headers)
    #request.set_proxy(choice(IPlist), 'http')
    hd = ''
    response_code = "0"
    while response_code != "200":
        try:
            number +=1
            print number
            response = urllib2.urlopen(request, timeout=2)
            response_code = str(response.getcode())
            print response_code
            if response_code == '404':
                return
            hd = response.read()
        except:
            pass
    # print hd
    soup = BeautifulSoup(hd,'lxml')
    lines = soup.select(" div.abstract ")
    file3 = file('E:\\zhuanli\\yuyin\\' + id + "_desc", 'a+')
    for line in lines:
        print line.get_text()
        file3.write(line.get_text())
    file3.close()


# 权利要求
def clms(IPlist, id):
    global number
    url1 = 'http://www.patexplorer.com/patent/view/'+id+'/detail/clms?_=' + get_time()
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'
    # headers['Cookie'] = '__jsluid=b96693d21e33e599750c8b14263094d5; UM_distinctid=15d5aee2a032df-079a7a03674693-474b0421-100200-15d5aee2a04762; CNZZDATA1253901093=720767245-1500466963-null%7C1501811796; Hm_lvt_1761fabf3c988e7f04bec51acd4073f4=1500469144,1501815\
    # 38; Hm_lpvt_1761fabf3c988e7f04bec51acd4073f4=1501815927; td_cookie=18446744069520568683'
    headers['Referer'] = 'http://www.patexplorer.com/results/s.html?sc=63&q=%28ad%3A%5B19480801+TO+20170808%5D%29&fq=type%3A%28cn_in%29&type=s&sort=&sortField='
    #headers["X-Forwarded-For"] = choice(IPlist)
    request = urllib2.Request(url1, headers=headers)
    #request.set_proxy(choice(IPlist), 'http')
    hd = ''
    response_code = "0"
    while response_code != "200":
        try:
            number +=1
            print number
            response = urllib2.urlopen(request, timeout=2)
            response_code = str(response.getcode())
            print response_code
            if response_code == '404':
                return
            hd = response.read()
        except:
            pass
    # print hd
    soup = BeautifulSoup(hd,'lxml')
    lines = soup.select(" div.abstract > div.sub > p ")
    file2=file('E:\\zhuanli\\yuyin\\'+id+"_clms", 'a+')
    for line in lines:
        print line.get_text()
        file2.write(line.get_text())
    file2.close()


# 著作项
def abst(IPlist, id):
    global number
    url0 = 'http://www.patexplorer.com/patent/view/'+id+'/detail/abst?_=' +get_time()
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'
    #headers['Cookie'] = '__jsluid=b96693d21e33e599750c8b14263094d5; UM_distinctid=15d5aee2a032df-079a7a03674693-474b0421-100200-15d5aee2a04762; CNZZDATA1253901093=720767245-1500466963-null%7C1501811796; Hm_lvt_1761fabf3c988e7f04bec51acd4073f4=1500469144,1501815\
    #838; Hm_lpvt_1761fabf3c988e7f04bec51acd4073f4=1501815927; td_cookie=18446744069520568683'
    headers['Referer'] = 'http://www.patexplorer.com/results/s.html?sc=63&q=%28ad%3A%5B19480801+TO+20170808%5D%29&fq=type%3A%28cn_in%29&type=s&sort=&sortField='
    #headers["X-Forwarded-For"] = choice(IPlist)
    request = urllib2.Request(url0, headers=headers)
    #request.set_proxy(choice(IPlist), 'http')
    hd = ''
    response_code = "0"
    while response_code != "200":
        try:
            number +=1
            print number
            response = urllib2.urlopen(request, timeout=2)
            response_code = str(response.getcode())
            print response_code
            if response_code == '404':
                return
            hd = response.read()
        except:
            pass
    # print hd
    soup = BeautifulSoup(hd,'lxml')
    lines = soup.select(" ul.abst-info > li ")
    file1 = file('E:\\zhuanli\\yuyin\\' + id + "_abst", 'a+')
    for line in lines:
        print line.get_text()
        file1.write(line.get_text().replace("\n", ""))
        file1.write("\n")
    lines_1 = soup.select(" div.abstract ")
    for line_1 in lines_1:
        print line_1.get_text()
        file1.write(line_1.get_text())
        file1.write("\n")
        #file1.flush()
    file1.close()


def t3(IPlist, id):
    time.sleep(1.1)
    abst(IPlist, id)
    time.sleep(1.2)
    clms(IPlist, id)
    time.sleep(1.1)
    desc(IPlist, id)
    time.sleep(1.3)
    pdf(IPlist, id)
    time.sleep(1.5)
    statues(IPlist, id)


def t2(IPlist, i):
    global number
    url = 'http://www.patexplorer.com/results/list'
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'
    #headers['Cookie'] = '__jsluid=b96693d21e33e599750c8b14263094d5; UM_distinctid=15d5aee2a032df-079a7a03674693-474b0421-100200-15d5aee2a04762; CNZZDATA1253901093=720767245-1500466963-null%7C1501811796; Hm_lvt_1761fabf3c988e7f04bec51acd4073f4=1500469144,1501815\
    #838; Hm_lpvt_1761fabf3c988e7f04bec51acd4073f4=1501815927; td_cookie=18446744069520568683'
    headers['Referer'] = 'http://www.patexplorer.com/results/s.html?sc=63&q=%28ad%3A%5B19480801+TO+20170808%5D%29&fq=type%3A%28cn_in%29&type=s&sort=&sortField='
    #headers["X-Forwarded-For"] = choice(IPlist)
    data = {"sc": "63", 'q':'语音', \
                     'sort': '', 'sortField':'', \
                     'fq':"type:(cn_in) AND ls1_1:(审中 OR 有效专利) AND pd:[20000101 to 20170812]",'pageSize':'100', \
                     'pageIndex':str(i), 'type':'s', 'merge':'no-merge'}
    values = urllib.urlencode(data)
    request = urllib2.Request(url, values, headers=headers)
    #request.set_proxy(choice(IPlist), 'http')
    response_code = "0"
    hd = ''
    print "t2:"
    num_1=1
    while response_code != "200":
        number += 1
        print number
        response = urllib2.urlopen(request, timeout=3)
        print num_1
        num_1 += 1
        response_code = str(response.getcode())
        print response_code
        hd = response.read()


    # print hd
    json_h=json.loads(hd)
    # print 'cubePatentSearchResponse:', json_h['cubePatentSearchResponse']
    #　print 'Md5Map:', json_h['Md5Map']
    print "total_hits:", json_h['cubePatentSearchResponse']['total_hits']
    # print "body:", json_h['cubePatentSearchResponse']['body']
    for lines in json_h['cubePatentSearchResponse']['documents']:
        #　print lines
        # print lines['field_values']['id']
        time.sleep(3.1)
        t3(IPlist, lines['field_values']['id'])
    j = int(json_h['cubePatentSearchResponse']['total_hits'])

    while 100 * i < j:
        i += 1
        t2(IPlist, i)


def t1():
    url = 'http://www.patexplorer.com/results/list'
    # url='http://www.patexplorer.com/results/s.html?sc=63&q=%28ad%3A%5B19480801+TO+20170808%5D%29&fq=type%3A%28cn_in%29&type=s&sort=&sortField=#/100/5'
    c = pycurl.Curl()
    c.setopt(pycurl.CAINFO, certifi.where())
    c.setopt(c.URL, url)
    b = StringIO.StringIO()
    c.setopt(pycurl.WRITEFUNCTION, b.write)
    c.setopt(pycurl.ACCEPTTIMEOUT_MS, 3000)
    # c.setopt(pycurl.HTTPPROXYTUNNEL)
    c.setopt(pycurl.TIMEOUT_MS, 3000)
    c.setopt(c.HTTPHEADER,
             ["Content-Type: application/json; charset=utf-8",
              "X-Requested-With:XMLHttpRequest",
              "Referer:http://www.patexplorer.com/results/s.html?sc=63&q=%28ad%3A%5B19480801+TO+20170808%5D%29&fq=type%3A%28cn_in%29&type=s&sort=&sortField="])
    c.setopt(pycurl.USERAGENT,
             "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36")
    # c.setopt(pycurl.PROXY, choice(IPlist))
    '''post_data_dic = {"sc": "63", 'q':'(ad:[19480801 TO 20170808])', \
                     'sort': '', 'sortField':'', \
                     'fq':"type:(cn_in)",'pageSize':'10', \
                     'pageIndex':'2', 'type':'s', 'merge':'no-merge'}

    c.setopt(c.POSTFIELDS, urllib.urlencode(post_data_dic))
    '''
    c.perform()
    hf = b.getvalue()
    print hf


if __name__ == "__main__":
    print "start"
    list_r = []
    list_r = getList()
    print list_r.__len__()
    #t1()
    t2(list_r, 1)
    #t3()
