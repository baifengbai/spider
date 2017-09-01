# -*- coding: utf-8 -*
# 高考志愿的每省市自治区的2012-2017的各院校分数线
import pycurl
import certifi
import StringIO
import time
import json
import sys

reload(sys)
sys.setdefaultencoding('utf8')


def dddd(i):
    file1 = file("E:\\school\\schoolprovince\\schoolgrade4", 'a+')
    try:
        url = 'http://data.api.gkcx.eol.cn/soudaxue/queryProvinceScore.html?messtype=jsonp&callback=jQuery183005728720230680184_1500627169216&provinceforschool=&schooltype=&page=' + str(
            i) + '&size=10&keyWord=&schoolproperty=&schoolflag=&province=&fstype=&zhaoshengpici=&fsyear=2016&_=1500627169874'
        url = "http://data.api.gkcx.eol.cn/soudaxue/queryProvinceScore.html?messtype=jsonp&callback=jQuery1830341254894635894_1500708869744&provinceforschool=&schooltype=&page=" + str(
            i) + "&size=10&keyWord=&schoolproperty=&schoolflag=&province=&fstype=&zhaoshengpici=&fsyear=&_=1500708873741"
        c = pycurl.Curl()
        c.setopt(pycurl.CAINFO, certifi.where())
        c.setopt(c.URL, url)
        b = StringIO.StringIO()
        c.setopt(pycurl.WRITEFUNCTION, b.write)
        c.perform()
        pic = b.getvalue()
        # print pic
        hjson = json.loads(str(pic).split("(")[1][:-2])
        num = hjson['totalRecord']['num']
        print num

        for school in hjson['school']:
            # print school
            new_count = school['schoolname'] + "*" + school[
                'localprovince'] + "*" + \
                        school['studenttype'] + "*" + school['year'] + "*" + \
                        school[
                            'batch'] + "*" + school['var'] + "*" + school[
                            'var_score'] + "*" + school['max'] + "*" + school[
                            'min'] + "*" + school['num'] + "*" + school[
                            'schoolid'] + "\n"
            print new_count
            file1.write(new_count)

        if int(num) > 10:
            # a=num/10+1
            while 10 * i < int(num):
                i = i + 1
                time.sleep(0.3)
                url = "http://data.api.gkcx.eol.cn/soudaxue/queryProvinceScore.html?messtype=jsonp&callback=jQuery1830341254894635894_1500708869744&provinceforschool=&schooltype=&page=" + str(
                    i) + "&size=10&keyWord=&schoolproperty=&schoolflag=&province=&fstype=&zhaoshengpici=&fsyear=&_=1500708873741"
                c = pycurl.Curl()
                c.setopt(pycurl.CAINFO, certifi.where())
                c.setopt(c.URL, url)
                b = StringIO.StringIO()
                c.setopt(pycurl.WRITEFUNCTION, b.write)
                c.perform()
                pic = b.getvalue()
                # print pic
                hjson = json.loads(str(pic).split("(")[1][:-2])
                for school in hjson['school']:
                    # print school
                    new_count = school['schoolname'] + "*" + school[
                        'localprovince'] + "*" + school['studenttype'] + "*" + \
                                school[
                                    'year'] + "*" + school['batch'] + "*" + \
                                school[
                                    'var'] + "*" + school[
                                    'var_score'] + "*" + str(
                        school[
                            'max']) + "*" + str(school['min']) + "*" + school[
                                    'num'] + "*" + school['schoolid'] + "\n"
                    print new_count
                    file1.write(new_count)
                    if i % 100 == 0:
                        file1.flush()


    except Exception:
        file1.close()
        time.sleep(20)
        dddd(i)
    file1.close()


if __name__=="__main__":

    i=14587
    dddd(i)