# -*- coding: utf-8 -*
# xxxxxx
import pycurl
import certifi
import StringIO
import time
import json
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
url='http://adv.soopat.com/Home/Result?SearchWord=FLH%3A(F01B)'
url = "http://data.api.gkcx.eol.cn/soudaxue/querySpecialtyScore.html?\
messtype=jsonp&callback=jQuery1830341254894635894_1500708869744&provinceforschool=&schooltype=&page=97967" \
      "&size=20&keyWord=&schoolproperty=&schoolflag=&province=&fstype=&zhaoshengpici=&fsyear=&zytype=&_=1500708873741"
c = pycurl.Curl()
c.setopt(pycurl.CAINFO, certifi.where())
c.setopt(c.URL, url)
b = StringIO.StringIO()
c.setopt(pycurl.WRITEFUNCTION, b.write)
c.perform()
pic = b.getvalue()
# print pic
hjson = json.loads(str(pic).split("44(")[1][:-2])
for school in hjson['school']:
    # print school
    new_count = str(school['schoolname']) + "*" + str(school['specialtyname']) \
                + "*" + str(school[ 'localprovince']) + "*" + str(school['studenttype']) + "*" + \
                str(school[ 'year']) + "*" + str(school['batch']) + "*" + \
                str(school['var']) + "*" + str(school['var_score']) + "*" + str(school['max']) + "*" +\
                str(school['min']) + "*" + str(school['schoolid'])
    print new_count