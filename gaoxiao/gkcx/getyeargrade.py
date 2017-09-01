# -*- coding: utf-8 -*
#
import pycurl
import certifi
import StringIO
import time
import json
import sys

reload(sys)
sys.setdefaultencoding('utf8')
i=1
url="http://data.api.gkcx.eol.cn/soudaxue/queryProvince.html?messtype=jsonp&callback=jQuery183045643628536390723_1500605796931&luqutype3=&province3=&year3=2012&luqupici3=&page="+str(i)+"&size=10&_=1500605797927"
c = pycurl.Curl()
c.setopt(pycurl.CAINFO, certifi.where())
c.setopt(c.URL, url)
b = StringIO.StringIO()
c.setopt(pycurl.WRITEFUNCTION, b.write)
c.perform()
pic = b.getvalue()
#print pic
hjson = json.loads(str(pic).split("(")[1][:-2])
num=hjson['totalRecord']['num']
print num
file1=file("E:\\school\\schoolprovince\\grade",'a+')
for school in hjson['school']:
    #print school
    new_count=school['province']+ "*"+school['bath']+ "*"+school['type']+ "*"+school['score']+ "*"+school['year']+"\n"
    print new_count
    file1.write(new_count)

if int(num) >10:
    #a=num/10+1
    while 10*i<int(num):
        i=i+1
        url = "http://data.api.gkcx.eol.cn/soudaxue/queryProvince.html?messtype=jsonp&callback=jQuery183045643628536390723_1500605796931&luqutype3=&province3=&year3=2012&luqupici3=&page=" + str(
            i) + "&size=10&_=1500605797927"
        c = pycurl.Curl()
        c.setopt(pycurl.CAINFO, certifi.where())
        c.setopt(c.URL, url)
        b = StringIO.StringIO()
        c.setopt(pycurl.WRITEFUNCTION, b.write)
        c.perform()
        pic = b.getvalue()
        #print pic
        hjson = json.loads(str(pic).split("(")[1][:-2])
        for school in hjson['school']:
            #print school
            new_count=school['province'] + "*"+school['bath'] + "*"+ school['type'] + "*"+ school[
                'score'] +  "*"+school['year']+"\n"
            print new_count
            file1.write(new_count)

file1.close()