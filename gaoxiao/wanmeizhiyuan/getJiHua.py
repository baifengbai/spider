# -*- coding: utf-8 -*
# 完美志愿 招生计划最初版，作废
import urllib2
import sys
import time
import json
import telnetlib
from bs4 import BeautifulSoup
from multiprocessing import Pool
import multiprocessing
from random import choice

reload(sys)
sys.setdefaultencoding("utf-8")

Numm = 0
user_agent = []
user_agent.append('Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)')
user_agent.append('Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)')
user_agent.append('Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) ')
def tePro(lines, llst):
    try:
        telnetlib.Telnet(str(lines).split(":")[0],
                         port=str(lines).split(":")[1], timeout=2)
    except Exception:
        # print 'connect failed'
        pass
    else:
        # print 'success'
        llst.append(str(lines))


def getIPs():
    list1 = []
    url = 'http://www.66ip.cn/nmtq.php?getnum=100&isp=0&anonymoustype=4&start=&ports=&export=&ipaddress=&area=1&proxytype=1&api=66ip'
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'
    headers['Cookie'] = '__jsluid=b96693d21e33e599750c8b14263094d5; UM_distinctid=15d5aee2a032df-079a7a03674693-474b0421-100200-15d5aee2a04762; CNZZDATA1253901093=720767245-1500466963-null%7C1501811796; Hm_lvt_1761fabf3c988e7f04bec51acd4073f4=1500469144,1501815\
    838; Hm_lpvt_1761fabf3c988e7f04bec51acd4073f4=1501815927; td_cookie=18446744069520568683'
    try:
        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request)
    except Exception:
        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request)
    hd = response.read()
    lines = str(hd).split(r"<br />")
    print 'IP num:', lines.__len__()
    j = 1
    while j < lines.__len__()-1:
        list1.append(str(lines[j]).replace(" ", '').replace("\r\n\t\t", ''))
        j += 1
    mgr = multiprocessing.Manager()
    llst = mgr.list()
    pool = Pool(processes=6)
    for liness in range(0, 30):
        pool.apply_async(tePro, args=(list1[liness],llst))
    '''
        for liness in list:
        pool.apply_async(tePro, args=(liness,llst))
    '''
    pool.close()
    pool.join()
    return llst


def getList():
    i = 1
    list = []
    while i < 2:
        # list = []
        list = getIPs()
        print list.__len__()
        # tq.extend(list)
        i += 1
    return list


def get_time():
    time_now = repr(time.time()*1000)
    return time_now[:-2]


def getJihua(provine, pro_name, batch, bat_n, wenli, id, diploma, year, page, IPlist):
    time.sleep(1)
    global Numm
    Numm += 1
    print Numm
    headers = { 'User-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0', "X-Forwarded-For":choice(IPlist)}
    url = 'https://www.wmzy.com/api/school/enrollment-list?sch_id='+id+'&diploma='+str(diploma)+'&province='+str(provine) +\
        '&ty='+wenli+'&year='+str(year)+'&batch='+str(batch)+'&page=' +\
        str(page)+'&page_len=30&&_='+get_time()
    response_code = '0'
    hf = ''
    while response_code != '200':
        proxy = 'https://' + str(choice(IPlist))
        print proxy
        proxy_handler = urllib2.ProxyHandler({"https": proxy})
        opener = urllib2.build_opener(proxy_handler)
        urllib2.install_opener(opener)
        request = urllib2.Request(url, headers = headers)
        #request.set_proxy(choice(IPlist), 'http')
        #response_1 = opener.open(request)
        response_1 = urllib2.urlopen(request)
        response_code = str(response_1.getcode())
        print response_code
        hf = response_1.read()


    hjson = json.loads(hf)
    pages = hjson['listHTML']['enrollPagination']
    details = hjson['listHTML']['enrollPlan']
    new_c = ''
    # print details
    soup = BeautifulSoup(details, 'lxml')
    lines = soup.select(" td ")
    if lines.__len__() % 4 == 0:
        num1 = 0
        while num1 < lines.__len__():
            tt1 = lines[num1].get_text().replace("\n", '').replace(' ', '')
            tt2 = lines[num1+1].get_text().replace("\n", '').replace(' ', '')
            tt3 = lines[num1+2].get_text().replace("\n", '').replace(' ', '')
            tt4 = lines[num1+3].get_text().replace("\n", '').replace(' ', '')
            new_c = new_c+str(provine)+"*"+str(pro_name)+"*"+wenli+"*" \
                    + str(year)+"*"+str(batch)+"*"+bat_n+"*"+tt1+"*"+tt2+"*"+tt3\
                    + "*"+tt4+"\n"
            num1 += 4
    else:
        if '暂无数据，请切换年份或批次查看' in details:
            return ''
        file5 = file("other1", 'a+')
        file5.write(str(url)+'\n')
        file5.close()
    # print new_c
    # print pages
    # 此处需判断是否只有一页，若不是，则递归调用此函数
    soup1 = BeautifulSoup(pages,'lxml')
    linesq1 = soup1.select(" li ")
    # print 'linesq1'
    # print linesq1.__len__()
    pagenum = set()
    for line in linesq1:
        pagenum.add(line.get('data-page'))
    # print pagenum.__len__()
    # time.sleep(10)
    if pagenum.__len__() > 1 and page < pagenum.__len__():
        new_c = new_c+getJihua(provine, pro_name, batch, bat_n, wenli, id,\
                               diploma, year, page+1, IPlist)
    return new_c


def getDetail(name, url, diploma, id, IPlist):
    print name
    print url
    print diploma
    # print choice(IPlist)
    response_code = '0'
    hf = ''
    while response_code != '200':
        proxy = 'https://' + str(choice(IPlist))
        print proxy
        proxy_handler = urllib2.ProxyHandler({"https:":proxy})
        opener = urllib2.build_opener(proxy_handler)
        urllib2.install_opener(opener)
        header_h={'User-Agent': choice(user_agent), 'Host': 'www.wmzy.com', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.8', "X-Forwarded-For":choice(IPlist)}
        request = urllib2.Request(url, headers=header_h)
        #request.
        #request.set_proxy('182.141.44.197:9000', 'http')
        response = urllib2.urlopen(request)
        print response.getcode()
        response_code = str(response.getcode())
        hf = response.read()



    soup = BeautifulSoup(hf, 'lxml')
    soupt1 = soup.findAll(class_='sch-mod m-sch-enroll m-plan')
    # 判断是否存在计划模块，不存在则异常
    if soupt1.__len__() == 1:
        soup1 = BeautifulSoup(str(soupt1[0]), 'lxml')
        soupt2 = soup1.findAll(class_='select-ul hidden')
        # 判断是否四个隐藏都有，没有则异常
        if soupt2.__len__() == 4:
            soupprovince = BeautifulSoup(str(soupt2[0]), 'lxml')
            # 省市列表
            provines = soupprovince.select(" li ")

            soupbatch = BeautifulSoup(str(soupt2[3]), 'lxml')
            # 批次列表
            batchs = soupbatch.select(" li ")
            result = []
            for provine in provines:
                # print provine.get_text()
                # print provine.get('data-province')
                for batch in batchs:
                    # print batch.get_text()
                    # print batch.get("data-batch")
                    year = 2015
                    while year < 2018:
                        page = 1
                        tq = getJihua(provine.get('data-province'), \
                                      str(provine.get_text())[5:].replace("\n", ''),
                                      batch.get("data-batch"), \
                                      batch.get_text().replace("\n", ''),\
                                      'li', id,
                                      diploma, year, page, IPlist)
                        if tq == '':
                            pass
                        else:
                            result.append(tq)
                        # print result
                        # time.sleep(300)
                        tq1 = getJihua(provine.get('data-province'), \
                                       str(provine.get_text())[5:].replace("\n", ''),
                                       batch.get("data-batch"), \
                                       batch.get_text().replace("\n", ''), \
                                       'wen', id, diploma, year, page, IPlist)
                        if tq1 == '':
                            pass
                        else:
                            result.append(tq1)
                        year += 1
            path_out = "E:\\school\\jihua\\"+str(name)
            ipath_out = unicode(path_out, 'uth-8')
            file_out = file(ipath_out, 'a+')
            for line_out in result:
                file_out = file(line_out)
            file_out.close()
        else:
            # 若不是上述情况，则视为异常
            file4 = file('school-jihua-not4-ex', 'a+')
            file4.write(url)
            file4.write('\n')
            file4.close()
    else:
        # 若不是上述情况，则视为异常
        file3 = file('school-jihua-ex', 'a+')
        file3.write(url)
        file3.write('\n')
        file3.close()


if __name__ == '__main__':
    file1 = file('schoollist')
    IPlist = getList()
    j1 = 2000
    #IPlist = []
    for file_lines in file1:
        line = file_lines.split("*")
        # 判断是否用*进行分割，并只有一个*
        if line.__len__() == 2:
            name = line[0]
            href = line[1].replace("\n",'')
            diploma = '7'
            sp1 = href.split("/")
            url = 'https://www.wmzy.com/api/school-score/'+sp1[3]
            id = sp1[3].split('.')[0]
            if 'diploma'in href:
                diploma = '5'
            if Numm > j1:
                j1 += 2000
                IPlist = getList()
            getDetail(name, url, diploma, id, IPlist)
            # 测试用暂停
            # time.sleep(20)
        else:
            # 若不是上述情况，则视为异常
            file2 = file('list-ex', 'a+')
            file2.write(file_lines)
            file2.write('\n')
            file2.close()
    file1.close()
