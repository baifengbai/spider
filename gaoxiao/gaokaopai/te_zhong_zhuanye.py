# -*- coding: utf-8 -*-
""" 高考派的硕士点数，博士点数，重点学科数，特色专业和重点专业"""
import sys
import urllib2
import time
from bs4 import BeautifulSoup
import pymysql
import random
import ssl


reload(sys)
sys.setdefaultencoding('utf-8')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit'
                  '/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 '
                  'Safari/537.36',
    'Cookie': "aliyungf_tc=AQAAANlSJG7wcQoAWVcHJI5H5JbNZUWP; "
              "acw_tc=AQAAAKVI6Q9iHQsAWVcHJMAZMIfAv79C; "
              "PHPSESSID=t7hq4rmr8gbravvcjpf55q57u1; "
              "Hm_lvt_c2c1aeb9dd53d590e8d4109d912eed04=1501135391,"
              "1501135933,1501136310,1501139056; Hm_lpvt_c2c1aeb9d"
              "d53d590e8d4109d912eed04=1501585004; appAdvertisemen"
              "t=hasClose; suid=3250003291; SERVERID=a59909634875"
              "bd0f1f0d1870496b3361|1503560205|1503556148; _ga=G"
              "A1.2.375727910.1499932018; _gid=GA1.2.289594526."
              "1503478662; Hm_lvt_b160b2fb030578dd4378d9630504cf"
              "2c=1501740962,1503558249; Hm_lpvt_b160b2fb030578d"
              "d4378d9630504cf2c=1503560200; td_cookie=184467440"
              "71264922585",
    'Referer': 'http://www.gaokaopai.com/daxue-0-0-0-0-0-0-0--p-1.html',
    'Upgrade-Insecure-Requests': '1',
    'Host': 'www.gaokaopai.com',
    "Accept - Encoding": "gzip, deflate",
    "Accept - Language": "zh - CN, zh;q = 0.8"}


def get_list():
    list_t = []
    ci = 0
    while list_t.__len__() < 20:
        try:
            list_t = []
            # IP_grade = {}
            conn = pymysql.connect(host='172.31.8.10', port=3306,
                                   user='jiezhang',
                                   password='jiezhang', db='zhiyuan',
                                   charset='utf8')
            cursor = conn.cursor()
            qi = ci * 20 * 20
            zhi = 20 * 20
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
    if list_t.__len__() > 3 * 20:
        return random.sample(list_t, 3 * 20)
    else:
        return list_t


def get_school_zz(url_s, name, li_shu, num_zhongdain, num_shuo, num_bo):
    proxy_handler = urllib2.ProxyHandler({"https": random.choice(get_list())})
    opener = urllib2.build_opener(proxy_handler)
    request = urllib2.Request(url_s, headers=headers)
    print random.choice(get_list())
    # request.set_proxy(random.choice(get_list()), 'https')

    try:
        response = opener.open(request)
    except:
        return 0
    hd = response.read()
    # print hd

    soup = BeautifulSoup(hd, 'lxml')
    zhuan_ye = soup.select(" div.modContent ")
    path = "E:\\school\\gaokaopai\\zhong_zhuan\\" + str(name)
    path_u = unicode(path, 'utf-8')
    file_2 = file(path_u, 'a+')
    file_2.write(str(name))
    file_2.write("*&#")
    file_2.write(li_shu)
    file_2.write("*&#")
    file_2.write(num_zhongdain)
    file_2.write("*&#")
    file_2.write(num_shuo)
    file_2.write("*&#")
    file_2.write(num_bo)
    if zhuan_ye.__len__() == 1:
        file_2.write("*&#")
        file_2.write(str(zhuan_ye[0]))
    file_2.close()
    return 1

def get_school_list(url_list):

    request = urllib2.Request(url_list, headers=headers)
    response = urllib2.urlopen(request)
    hd = response.read()
    # print hd

    soup = BeautifulSoup(hd, 'lxml')
    s_list = soup.select(" div.con ")
    print s_list.__len__()
    if s_list.__len__() == 0:
        print "error"
        return 0
    else:
        for i_s in range(s_list.__len__()):
            soup_s = BeautifulSoup(str(s_list[i_s]), 'lxml')
            sc_1 = soup_s.findAll(class_="s s1")
            print str(sc_1[0].get_text()) \
                .replace("\r\n", '') \
                .replace("\n", '') \
                .replace("\t", '') \
                .replace(" ", '')
            new_1 = str(sc_1[0].get_text()) \
                .replace("\r\n", '') \
                .replace("\n", '') \
                .replace("\t", '') \
                .replace(" ", '')
            num_zhongdain = str(new_1.split("重点学科数：")[1]).replace("个", '')
            li_shu = str(new_1.split("重点学科数：")[0]).split("隶属：")[1]
            print num_zhongdain, li_shu

            sc_2 = soup_s.findAll(class_="s s2")
            print str(sc_2[0].get_text()) \
                .replace("\r\n", '') \
                .replace("\n", '') \
                .replace("\t", '') \
                .replace(" ", '')
            new_2 = str(sc_2[0].get_text()) \
                .replace("\r\n", '') \
                .replace("\n", '') \
                .replace("\t", '') \
                .replace(" ", '')
            num_shuo = str(new_2.split("博士点数：")[0]).split("硕士点数：")[1]. \
                replace("个", '')
            num_bo = new_2.split("博士点数：")[1].replace("个", '')
            print num_shuo, num_bo

            title = soup_s.select(" h3 > a ")
            if title.__len__() == 1:
                print title[0].get("href")
                tr_1 = get_school_zz(title[0].get("href"), title[0].get_text(),
                              li_shu, num_zhongdain,
                              num_shuo, num_bo)
                if tr_1 == 1:
                    pass
                else:
                    tr_1 = get_school_zz(title[0].get("href"),
                                         title[0].get_text(),
                                         li_shu, num_zhongdain,
                                         num_shuo, num_bo)

            time.sleep(0.2)
        return 1


def main():
    print '88'
    i = 1
    while i < 232:

        url_list = "http://www.gaokaopai.com/daxue-0-0-0-0-0-0-0--p-" + \
                   str(i) + ".html"
        flag = get_school_list(url_list)
        if flag == 1:
            i += 1
        else:
            pass


if __name__ == "__main__":
    main()
