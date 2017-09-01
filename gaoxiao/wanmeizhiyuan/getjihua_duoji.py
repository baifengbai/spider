# -*- coding: utf-8 -*
# 作废
import urllib2
import sys
import time
import json
import telnetlib
from bs4 import BeautifulSoup
from multiprocessing import Pool
import multiprocessing
from random import choice
import pycurl
import certifi
import StringIO
import pymysql
reload(sys)
sys.setdefaultencoding("utf-8")

j1 = 50
IP_grade = {}
Numm = 0
user_agent = []
user_agent.append('Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')
user_agent.append('Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36')
user_agent.append('Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3226.400 QQBrowser/9.6.11681.400')
user_agent.append('Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36')
user_agent.append('Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0')


def change_grade(IP_grade):
    print " 更新数据库"
    conn = pymysql.connect(host='172.31.8.10', port=3306, user='jiezhang',
                           password='jiezhang', db='zhiyuan', charset='utf8')
    cursor = conn.cursor()
    print "genxin:", IP_grade
    try:
        sql = "UPDATE IPproxy SET grade = %s WHERE host = %s and port = %s"
        print sql
        for line_ip in IP_grade:
            # print line_ip
            cursor.execute(sql, (int(IP_grade[line_ip]), str(line_ip).split(":")[0], str(line_ip).split(":")[1]))
        conn.commit()
    except:
        print " IP 数据库更新失败 一次"
        pass
    cursor.close()
    conn.cursor()
    print "更新完成"


def getList():
    # global IP_grade
    IP_grade = {}
    list = []
    conn = pymysql.connect(host='172.31.8.10', port=3306, user='jiezhang',
                           password='jiezhang', db='zhiyuan', charset='utf8')
    cursor = conn.cursor()
    sql = "SELECT * FROM IPproxy ORDER BY grade DESC LIMIT 0,200"
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        list.append(row[0]+":"+row[1])
        # print row
        temp = row[0]+":"+row[1]
        IP_grade[temp] = str(row[2])
    cursor.close()
    conn.close()
    # print IP_grade
    return list, IP_grade


def get_time():
    time_now = repr(time.time()*1000)
    return time_now[:-2]


def getJihua(provine, pro_name, batch, bat_n, wenli, id, diploma, year, page, IPlist, IP_dict, Num_x):
    global j1
    time.sleep(0.2)
    headers = { 'User-agent': choice(user_agent), "X-Forwarded-For":choice(IPlist)}
    url = 'https://www.wmzy.com/api/school/enrollment-list?sch_id='+id+'&diploma='+str(diploma)+'&province='+str(provine) +\
        '&ty='+wenli+'&year='+str(year)+'&batch='+str(batch)+'&page=' +\
        str(page)+'&page_len=30&&_='+get_time()
    response_code = '0'
    hf = ''
    while response_code != '200':
        try:
            Num_x.x += 1
            print Num_x.x
            if Num_x.x > Num_x.j:
                j1 += 50
                Num_x.j = j1
                print "IP_dict:", IP_dict
                change_grade(IP_dict.copy())
                IPlist.clear()
                # IP_grade.clear()
                IPlist , IP_grade = getList()
                print "IP_grade:", IP_grade
                print " IP_dict:", IP_dict
                IP_dict.clear()
                IP_dict = IP_grade.copy()
                print " IP_dict:", IP_dict
            this_ip = choice(IPlist)
            # proxy = 'https://' + str(choice(IPlist))
            print this_ip
            c = pycurl.Curl()
            c.setopt(pycurl.CAINFO, certifi.where())
            c.setopt(c.URL, url)
            b = StringIO.StringIO()
            c.setopt(pycurl.WRITEFUNCTION, b.write)
            c.setopt(pycurl.ACCEPTTIMEOUT_MS, 2500)
            # c.setopt(pycurl.HTTPPROXYTUNNEL)
            c.setopt(pycurl.TIMEOUT_MS, 2500)
            c.setopt(c.HTTPHEADER,
                     ["Content-Type: application/json; charset=utf-8",
                      "X-Requested-With:XMLHttpRequest",
                      "X-Forwarded-For:" + this_ip])
            c.setopt(pycurl.USERAGENT, choice(user_agent))
            c.setopt(pycurl.PROXY, this_ip)
            c.perform()
            print c.getinfo(c.HTTP_CODE)
            response_code = str(c.getinfo(c.HTTP_CODE))
            hf = b.getvalue()
        except:
            try:
                # print IP_dict
                print IP_dict[this_ip]
                grade_y = IP_dict[this_ip]
                grade_n=int(grade_y) - 1
                IP_dict[this_ip] = str(grade_n)
                this_ip = choice(IPlist)
            except:
                print " num exception 2"
                pass
            pass
    grade_y = IP_dict[this_ip]
    grade_n = int(grade_y) + 1
    IP_dict[this_ip] = str(grade_n)
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
                               diploma, year, page+1, IPlist, IP_dict, Num_x)
    return new_c


def getDetail(name, url, diploma, id, IPlist, IP_grade):
    global j1
    global Numm
    print name
    print url
    print diploma
    response_code = '0'
    hf = ''
    mgr = multiprocessing.Manager()
    IP_dict = mgr.dict()
    Num_x = mgr.Namespace()
    Num_x.x = Numm
    Num_x.j = j1
    IP_dict = IP_grade.copy()
    while response_code != '200':
        try:
            Num_x.x += 1
            print Num_x.x
            if Num_x.x > Num_x.j:
                j1 += 50
                Num_x.j = j1
                change_grade(IP_grade)
                # IPlist.clear()
                # IP_grade.clear()

                IPlist , IP_grade = getList()
                print " IP_dict:", IP_dict
                IP_dict.clear()
                IP_dict = IP_grade.copy()
                print " IP_dict:", IP_dict
            this_ip = choice(IPlist)
            print this_ip
            # proxy = 'https://' + str(choice(IPlist))
            # print proxy
            c = pycurl.Curl()
            c.setopt(pycurl.CAINFO, certifi.where())
            c.setopt(c.URL, url)
            b = StringIO.StringIO()
            c.setopt(pycurl.WRITEFUNCTION, b.write)
            c.setopt(pycurl.ACCEPTTIMEOUT_MS, 5000)
            # c.setopt(pycurl.HTTPPROXYTUNNEL)
            c.setopt(pycurl.TIMEOUT_MS, 5000)
            c.setopt(c.HTTPHEADER,
                     ["Content-Type: application/json; charset=utf-8",
                      "X-Requested-With:XMLHttpRequest",
                      "X-Forwarded-For:" + this_ip])
            c.setopt(pycurl.USERAGENT, choice(user_agent))
            # this_ip = choice(IPlist)
            c.setopt(pycurl.PROXY, this_ip)
            c.perform()
            print c.getinfo(c.HTTP_CODE)
            response_code = str(c.getinfo(c.HTTP_CODE))
            hf = b.getvalue()
            if response_code == '301':
                c.setopt(c.URL, 'https://www.wmzy.com'+str(hf).split("\"")[1])
                c.perform()
                response_code = str(c.getinfo(c.HTTP_CODE))
                hf = b.getvalue()
        except:
            try:
                # print IP_grade
                grade_y = IP_dict[this_ip]
                print grade_y
                grade_n=int(grade_y) - 1
                IP_dict[this_ip] = str(grade_n)
                this_ip = choice(IPlist)
            except:
                print " num exception 1"
                pass
            pass
    grade_y = IP_dict[this_ip]
    grade_n = int(grade_y) + 1
    IP_dict[this_ip] = str(grade_n)
    # print hf
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

            pool = Pool(processes=10)
            for provine in provines:
                # print provine.get_text()
                # print provine.get('data-province')
                for batch in batchs:
                    # print batch.get_text()
                    # print batch.get("data-batch")
                    year = 2015
                    while year < 2018:
                        page = 1
                        tq_r = pool.apply_async(getJihua, args=(provine.get('data-province'), \
                                      str(provine.get_text())[5:].replace("\n", ''), batch.get("data-batch"), \
                                      batch.get_text().replace("\n", ''),\
                                      'li', id, diploma, year, page, IPlist, IP_dict, Num_x,))
                        tq = tq_r.get()
                        '''
                        tq = getJihua(provine.get('data-province'), \
                                      str(provine.get_text())[5:].replace("\n", ''),
                                      batch.get("data-batch"), \
                                      batch.get_text().replace("\n", ''),\
                                      'li', id,
                                      diploma, year, page, IPlist)
                        '''
                        if tq == '':
                            pass
                        else:
                            result.append(tq)
                        # print result
                        # time.sleep(300)

                        tq1_r = pool.apply_async(getJihua, (provine.get('data-province'), \
                                       str(provine.get_text())[5:].replace("\n", ''), batch.get("data-batch"), \
                                       batch.get_text().replace("\n", ''), \
                                       'wen', id, diploma, year, page, IPlist, IP_dict, Num_x,))
                        tq1 = tq1_r.get()
                        '''tq1 = getJihua(provine.get('data-province'), \
                                       str(provine.get_text())[5:].replace("\n", ''),
                                       batch.get("data-batch"), \
                                       batch.get_text().replace("\n", ''), \
                                       'wen', id, diploma, year, page, IPlist)
                        '''
                        if tq1 == '':
                            pass
                        else:
                            result.append(tq1)
                        year += 1
            pool.close()
            pool.join()
            Numm = Num_x.x
            IP_grade = IP_dict
            path_out = "E:\\school\\jihua\\"+str(name)
            ipath_out = unicode(path_out, 'utf-8')
            file_out = file(ipath_out, 'a+')
            for line_out in result:
                file_out .write(line_out)
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
    file1 = file('schoollist1')
    IP_grade = {}
    IPlist, IP_grade = getList()
    j1 = 50
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
            getDetail(name, url, diploma, id, IPlist, IP_grade)
            # 测试用暂停
            # time.sleep(20)
        else:
            # 若不是上述情况，则视为异常
            file2 = file('list-ex', 'a+')
            file2.write(file_lines)
            file2.write('\n')
            file2.close()
    file1.close()
