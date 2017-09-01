# -*- coding: utf-8 -*-
# 完美志愿 招生计划第二版
import urllib2
import sys
import time
import json
from bs4 import BeautifulSoup
from multiprocessing import Pool
from random import choice
import random
import pymysql

reload(sys)
sys.setdefaultencoding("utf-8")

j1 = 20
user_agent = []
number = 20
user_agent.append('Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/59.0.3071.115 Safari/537.36')
user_agent.append('Mozilla/5.0 (Windows NT 6.1; WOW64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/45.0.2454.101 Safari/537.36')
user_agent.append('Mozilla/5.0 (Windows NT 6.1; WOW64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/53.0.2785.104 Safari/537.36 '
                  'Core/1.53.3226.400 QQBrowser/9.6.11681.400')
user_agent.append('Mozilla/5.0 (Windows NT 6.1; WOW64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/59.0.3071.104 Safari/537.36')
user_agent.append('Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) '
                  'Gecko/20100101 Firefox/22.0')


# 得到number个有效的ip
def get_list():
    global number
    list_t = []
    ci = 0
    while list_t.__len__() < number:
        try:
            list_t = []
            # IP_grade = {}
            conn = pymysql.connect(host='127.0.0.1', port=3306,
                                   user='xx',
                                   password='xxxx', db='zhiyuan',
                                   charset='utf8')
            cursor = conn.cursor()
            qi = ci * number * 20
            zhi = number * 20
            sql = "SELECT * FROM IPproxy2 ORDER BY grade DESC LIMIT %s, %s"
            cursor.execute(sql, (qi, zhi))
            rows = cursor.fetchall()
            for row in rows:
                list_t.append(row[0] + ":" + row[1])
            cursor.close()
            conn.close()
            ci += 1
        except:
            print "提取ip异常或没有足够的有效ip"
            time.sleep(10)
    # change_grade(grade)
    if list_t.__len__() > 3 * number:
        return random.sample(list_t, 3 * number)
    else:
        return list_t


def get_time():
    time_now = repr(time.time()*1000)
    return time_now[:-2]


def get_jihua(provine, pro_name, batch, bat_n, wenli, id, diploma, year, page):
    global j1
    global number

    IPlist = get_list()
    url = 'https://www.wmzy.com/api/school/enrollment-list?sch_id=' + \
          id + \
          '&diploma=' + str(diploma) + \
          '&province=' + str(provine) + \
          '&ty=' + wenli + \
          '&year=' + str(year) + \
          '&batch=' + str(batch) + \
          '&page=' + str(page) + \
          '&page_len=30&&_=' + get_time()
    response_code = '0'
    hf = ''
    this_ip = ""
    i_2 = 0
    while response_code != '200':
        try:
            i_2 += 1
            if i_2 > j1:
                i_2 = 0
                IPlist = get_list()

            this_ip = choice(IPlist)
            headers = {"Content-Type": "application/json; charset=utf-8",
                       "X-Requested-With": "XMLHttpRequest",
                       "X-Forwarded-For": this_ip,
                       "User-Agent": choice(user_agent)}
            proxy_handler = urllib2.ProxyHandler(
                {"https": random.choice(get_list())})
            opener = urllib2.build_opener(proxy_handler)

            request = urllib2.Request(url, headers=headers)
            response = opener.open(request, timeout=5)

            hf = response.read()
            response_code = str(response.getcode())
            print response_code

            if "您的访问频率似乎有点高，先歇歇吧" in str(hf):
                print "您的访问频率似乎有点高，先歇歇吧"
                response_code = "403"
        except:
            print "ip shi xiao 2:", this_ip
            this_ip = choice(IPlist)

    hjson = json.loads(hf)
    print hf
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
            new_c = (new_c + str(provine) + "*" +
                     str(pro_name) + "*" +
                     wenli + "*" +
                     str(year) + "*" +
                     str(batch) + "*" +
                     bat_n + "*" +
                     tt1 + "*" +
                     tt2 + "*" +
                     tt3 + "*" +
                     tt4 + "\n")
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
    lines_q1 = soup1.select(" li ")
    page_num = set()
    for line_1 in lines_q1:
        page_num.add(line_1.get('data-page'))
    if page_num.__len__() > 1 and page < page_num.__len__():
        new_c = (new_c + get_jihua(provine,
                                   pro_name,
                                   batch,
                                   bat_n,
                                   wenli,
                                   id,
                                   diploma,
                                   year,
                                   page+1))

    return str(new_c)


def get_detail(name, url, diploma, id):
    global j1
    global Numm
    global number
    print name
    print url
    print diploma
    IPlist = get_list()
    print IPlist.__len__()
    response_code = '0'
    hf = ''
    this_ip = ""
    i_1 = 0
    while response_code != '200':
        try:
            i_1 += 1
            if i_1 > j1:
                i_1 = 0
                IPlist = get_list()

            this_ip = choice(IPlist)
            headers = {"Content-Type": "application/json; charset=utf-8",
                       "X-Requested-With": "XMLHttpRequest",
                       "X-Forwarded-For": this_ip,
                       "User-Agent": choice(user_agent)}
            proxy_handler = urllib2.ProxyHandler(
                {"https": random.choice(get_list())})
            opener = urllib2.build_opener(proxy_handler)

            request = urllib2.Request(url, headers=headers)
            response = opener.open(request, timeout=5)

            hf = response.read()
            response_code = str(response.getcode())
            print response_code
        except:
            print "ip shi xiao 1:", this_ip
            this_ip = choice(IPlist)

    print hf

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
                        tq_r = pool.apply_async(get_jihua, args=(
                            provine.get('data-province'),
                            str(provine.get_text())[5:].replace("\n", ''),
                            batch.get("data-batch"),
                            batch.get_text().replace("\n", ''),
                            'li',
                            id,
                            diploma,
                            year,
                            page,))

                        print tq_r
                        tq = tq_r.get()
                        if tq == '':
                            pass
                        else:
                            result.append(tq)
                        # print result

                        tq1_r = pool.apply_async(get_jihua, (
                            provine.get('data-province'),
                            str(provine.get_text())[5:].replace("\n", ''),
                            batch.get("data-batch"),
                            batch.get_text().replace("\n", ''),
                            'wen',
                            id,
                            diploma,
                            year,
                            page, ))

                        tq1 = tq1_r.get()
                        if tq1 == '':
                            pass
                        else:
                            result.append(tq1)
                        year += 1

            pool.close()
            pool.join()
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
            get_detail(name, url, diploma, id)
        else:
            # 若不是上述情况，则视为异常
            file2 = file('list-ex', 'a+')
            file2.write(file_lines)
            file2.write('\n')
            file2.close()
    file1.close()
