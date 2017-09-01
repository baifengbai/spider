# -*- coding: utf-8 -*
"""阳光高考专业库的信息，毕业生规模规模"""
import urllib2
import urllib
from bs4 import BeautifulSoup
import re
import time
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


def get_detail(name, url_t):
    url_3 = "http://gaokao.chsi.com.cn"+url_t
    request_3 = urllib2.Request(url_3)
    response_3 = urllib2.urlopen(request_3)
    # print response_3.read()
    web_data_3 = response_3.read()
    soup_3 = BeautifulSoup(web_data_3, 'lxml')
    g_m = soup_3.select(" div.chartBYS ")
    if g_m.__len__() == 1:
        file_4 = file("E:\\school\\yangguanggaokao\\zhuanye\\z4", "a+")
        file_4.write(str(name))
        file_4.write("*")
        file_4.write(str(g_m[0].get_text()).replace("\n", ''))
        file_4.write("\n")
        file_4.close()


def get_speciality(id):
    url_2 = "http://gaokao.chsi.com.cn/zyk/zybk/specialityesByCategory.action"
    values_2 = {}
    values_2["key"] = id
    data_2 = urllib.urlencode(values_2)
    request_2 = urllib2.Request(url_2, data_2)
    response_2 = urllib2.urlopen(request_2)
    web_data_2 = response_2.read()
    # print web_data_2
    # print type(web_data_2)
    # print repr(web_data_2)
    wh = web_data_2
    soup_2 = BeautifulSoup(wh, 'lxml')
    l_lines = soup_2.select(" td > a ")
    print l_lines.__len__()
    l_line = 0
    while l_line < l_lines.__len__():
        print l_lines[l_line].get_text()
        print l_lines[l_line].get("href")
        time.sleep(1)
        get_detail(l_lines[l_line].get_text(), l_lines[l_line].get("href"))
        l_line += 3


if __name__ == "__main__":
    url = "http://gaokao.chsi.com.cn/zyk/zybk/xkCategory.action"
    values = {}
    # key = 105001,105002,105003,105004,105005,105006,105007,105008,105009,105010,105012,105013
    values['key'] = "105013"
    data = urllib.urlencode(values)
    request = urllib2.Request(url, data)
    response = urllib2.urlopen(request)
    # print response.read()
    web_data = response.read()
    soup = BeautifulSoup(web_data, "lxml")
    c_lines = soup.select(" li ")
    for c_line in c_lines:
        print c_line.get("id")
        get_speciality(c_line.get("id"))
