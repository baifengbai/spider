# -*- coding: utf-8 -*
#高考志愿的每省市自治区的2012-2017的各院校专业分数线
import pycurl
import certifi
import StringIO
import time
import json
import sys

i = 58864


def dddd(j):

    global i
    i=j
    print i
    file1 = file("E:\\school\\schoolprovince\\zhuanyegrade4", 'a+')
    url = "http://data.api.gkcx.eol.cn/soudaxue/querySpecialtyScore.html?messtype=jsonp&callback=jQuery1830341254894635894_1500708869744&provinceforschool=&schooltype=&page=" + str(
        i) + "&size=20&keyWord=&schoolproperty=&schoolflag=&province=&fstype=&zhaoshengpici=&fsyear=&zytype=&_=1500708873741"
    c = pycurl.Curl()
    c.setopt(pycurl.CAINFO, certifi.where())
    c.setopt(c.URL, url)
    b = StringIO.StringIO()
    c.setopt(pycurl.WRITEFUNCTION, b.write)
    c.perform()
    pic = b.getvalue()
    #print pic
    hjson = json.loads(str(pic).split("44(")[1][:-2])
    num = hjson['totalRecord']['num']
    print num

    for school in hjson['school']:
        # print school
        new_count = str(school['schoolname']) + "*" +str(school['specialtyname']) + "*" + str(school[
            'localprovince']) + "*" + \
                    str(school['studenttype']) + "*" + str(school['year']) + "*" + \
                    str(school[
                        'batch']) + "*" + str(school['var']) + "*" + str(school[
                        'var_score']) + "*" + str(school['max']) + "*" + str(school[
                        'min']) + "*" + str(school[
                        'schoolid']) + "\n"
        #print new_count
        file1.write(new_count)

    if int(num) > 20:
        # a=num/10+1
        while i < 62800:
            i = i + 1
            print i
            time.sleep(0.3)
            url = "http://data.api.gkcx.eol.cn/soudaxue/querySpecialtyScore.html?messtype=jsonp&callback=jQuery1830341254894635894_1500708869744&provinceforschool=&schooltype=&page=" + str(
                i) + "&size=20&keyWord=&schoolproperty=&schoolflag=&province=&fstype=&zhaoshengpici=&fsyear=&zytype=&_=1500708873741"
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
                new_count = str(school['schoolname']) + "*" + str(school['specialtyname']) + "*" + str(school[
                    'localprovince']) + "*" + str(school['studenttype']) + "*" + \
                            str(school[
                                'year']) + "*" + str(school['batch']) + "*" + \
                            str(school[
                                'var']) + "*" + str(school[
                                'var_score']) + "*" + str(
                    school[
                        'max']) + "*" + str(school['min']) + "*" + str(school['schoolid']) + "\n"
                #print new_count
                file1.write(new_count)
                if i % 200 == 0:
                    file1.flush()
    file1.close()



def xunhuan(j):
    global i
    i=j
    print "xunh"
    print i

    try:
        dddd(i)
    except Exception:
        print "sleep"
        time.sleep(30)
        xunhuan(i)


if __name__=="__main__":
    print i
    reload(sys)
    sys.setdefaultencoding('utf8')
    i=58864
    xunhuan(i)