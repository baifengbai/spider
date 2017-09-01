# -*- coding: utf-8 -*
#得到高考教育在线的大学名单
import time
import pycurl
import certifi
import StringIO
import json
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf8')

i = 1
url = "http://data.api.gkcx.eol.cn/soudaxue/queryschool.html?messtype=jsonp&callback=jQuery18306782865823359598_1500888441164&province=&schooltype=&page="+str(i)+"&size=30&keyWord1=&schoolprop=&schoolflag=&schoolsort=&schoolid=&_=1500888444135"
c = pycurl.Curl()
c.setopt(pycurl.CAINFO, certifi.where())
c.setopt(c.URL, url)
b = StringIO.StringIO()
c.setopt(pycurl.WRITEFUNCTION, b.write)
c.perform()
pic = b.getvalue()
# print pic
hjson = json.loads(str(pic).split("164(")[1][:-2])
num = hjson['totalRecord']['num']

print num
file1 = file("E:\\school\\schoolid",'a+')
for school in hjson['school']:
    # print school
    new_count = (str(school['schoolname']) + "*" +
                 str(school['province']) +"*" +
                 str(school[ 'schooltype']) + "*" +
                 str(school['schoolproperty']) + "*" +
                 str(school['schoolnature']) + "*" +
                 str(school['schoolid']) + "*" +
                 str(school['membership']) + "*" +
                 str(school['level']) + "*" +
                 str(school['guanwang']) + "*" +
                 str(school['f985']) + "*" +
                 str(school['f211']) + "*" +
                 str(school['edudirectly']) + "*" +
                 str(school['center'])+ "*" +
                 str(school['autonomyrs']) + "*" +
                 str(school['oldname']) + "\n")
    print new_count
    file1.write(new_count)

if int(num) > 30:
    # a=num/10+1
    while 30 * i < int(num):
        i = i + 1
        time.sleep(0.4)
        url ="http://data.api.gkcx.eol.cn/soudaxue/queryschool.html?messtype=jsonp&callback=jQuery18306782865823359598_1500888441164&province=&schooltype=&page="+str(i)+"&size=30&keyWord1=&schoolprop=&schoolflag=&schoolsort=&schoolid=&_=1500888444135"
        c = pycurl.Curl()
        c.setopt(pycurl.CAINFO, certifi.where())
        c.setopt(c.URL, url)
        b = StringIO.StringIO()
        c.setopt(pycurl.WRITEFUNCTION, b.write)
        c.perform()
        pic = b.getvalue()
        # print pic
        hjson = json.loads(str(pic).split("164(")[1][:-2])
        for school in hjson['school']:
            # print school
            new_count = str(school['schoolname']) + "*" + str(
                school['province']) + "*" + str(school[
                                                    'schooltype']) + "*" + \
                        str(school['schoolproperty']) + "*" + str(
                school['schoolnature']) + "*" + \
                        str(school[
                                'schoolid']) + "*" + str(
                school['membership']) + "*" + str(school[
                                                      'level']) + "*" + str(
                school['guanwang']) + "*" + str(school[
                                                    'f985']) + "*" + str(school[
                                                                             'f211']) + "*" + str(
                school[
                    'edudirectly']) + "*" + str(school[
                                                    'center']) + "*" + str(
                school[
                    'autonomyrs']) + "*" + str(school[
                                                   'oldname']) + "\n"
            print new_count
            file1.write(new_count)
file1.close()