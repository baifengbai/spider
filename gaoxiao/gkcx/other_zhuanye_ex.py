# -*- coding: utf-8 -*
# eol 另一种方法的专业分数 不充
import urllib2
import json
import sys
import time

reload(sys)
sys.setdefaultencoding("utf-8")


def get_detail(name, url):
    time.sleep(0.2)
    request = urllib2.Request(url)
    response_code = "0"
    hd = ""
    try:
        print url
        response = urllib2.urlopen(request, timeout=3)
        hd = response.read()
    except Exception:
        print url
        file3 = file("E:\\school\\schoolprovince\\iii\\ex\\ex_x_x_x_x_x", "a+")
        file3.write(str(url))
        file3.write("\n")
        file3.close()
        return

    if str(hd).startswith("<?xml version="):
        temp_1 = url.split("provinceScores")[1]
        province = temp_1.split("_")[1]
        wen_li = temp_1.split("_")[2]
        pi_c = temp_1.split("_")[3].replace(".xml", '')
        path = "E:\\school\\schoolprovince\\yyy\\" + \
               str(name).replace("\n", "") + "_" + str(province) + \
               "_"+str(wen_li) + "_" + str(pi_c)
        ipath = unicode(path,"utf-8")
        file2 = file(ipath, "a+")
        file2.write(hd)
        file2.close()


if __name__ == "__main__":
    file1 = file("E:\\school\\schoolprovince\\iii\\ex\\ex_x_x_x_x")
    file_2 = file('school_list')
    school = {}
    for name in file_2:
        school[name.split("*")[0]] = name.split("*")[1].replace("\n", '')
    for line in file1:
        #temp = line.split(".xml")
        #for xml in temp:
        name = line.split("provinceScores")[1].split("_")[0]
        get_detail(school[name], line.replace("\n", ''))
