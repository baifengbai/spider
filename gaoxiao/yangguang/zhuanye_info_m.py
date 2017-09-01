# -*- coding: utf-8 -*
'''阳光高考专业库的信息，包括专业就业率，专业男女比，相近专业'''
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
    jiu_ye = soup_3.select(" div.box_cnt ")
    # print jiu_ye[0].get_text()
    print repr(jiu_ye[0].get_text())
    pattern = re.compile('2014\(.+\)  2015\(.+\)  2016\(.+\)')
    temp = jiu_ye[0].get_text().replace(" ", '').replace(
        "\r\n", '').replace("\n", '').encode('utf-8')
    print temp
    match = re.search(pattern, temp)
    if match:
        print match.group()
        file_2 = file("E:\\school\\yangguanggaokao\\zhuanye\\z1", "a+")
        file_2.write(str(name)+"*")
        file_2.write(str(match.group()))
        file_2.write("\n")
        file_2.close()
    boy = soup_3.findAll(id="hid_boy")
    girl = soup_3.findAll(id="hid_girl")
    print boy[0].get("value")
    print girl[0].get("value")
    file_3 = file("E:\\school\\yangguanggaokao\\zhuanye\\z2", "a+")
    file_3.write(str(name)+"*")
    file_3.write(boy[0].get("value"))
    file_3.write("*")
    file_3.write(girl[0].get("value"))
    file_3.write("\n")
    file_3.close()
    xjzy = soup_3.select(" table.table_xjzy ")
    if xjzy.__len__() == 1:
        soup_4 = BeautifulSoup(str(xjzy[0]), 'lxml')
        zy = soup_4.select(" td > a ")
        l_zy = 0
        file_4 = file("E:\\school\\yangguanggaokao\\zhuanye\\z3", "a+")
        file_4.write(str(name))
        while l_zy < zy.__len__():
            print zy[l_zy].get_text()
            file_4.write("*")
            file_4.write(zy[l_zy].get_text().replace("\n", ''))
            l_zy += 2
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
