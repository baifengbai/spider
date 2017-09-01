# -*- coding: utf-8 -*
# 百度学校基本信息
import time
import urllib
import urllib2
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def kkqq(linest):
    time.sleep(1)
    print linest
    url = linest.split("*")[1].replace("\n", '')
    data = {}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36",
        'Referer': "https://baike.baidu.com/"}
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    # print response.read()
    hd = response.read()
    # print hd
    soup = BeautifulSoup(hd, 'lxml')
    lines = soup.select(" div.basic-info > dl > dt ")
    print lines.__len__()
    lines1 = soup.select(" div.basic-info > dl > dd ")
    print lines1.__len__()
    if lines.__len__() == lines1.__len__():
        i = 0
        path = 'E:\\school\\schoollist\\schoolinfo\\' + linest.split("*")[0]
        path1 = unicode(path, 'utf-8')
        file2 = file(path1, 'a+')

        new_count = []
        while i < lines.__len__():
            new_count.append(lines[i].get_text() + "$%" + lines1[i].get_text())

            i += 1
        print new_count
        outt = ''
        for liness in new_count:
            outt = outt + liness + "&*$"
        print outt[:-3]
        file2.write(outt[:-3])
        file2.close()
        # time.sleep(10)


def getinfo():
    file1=open('E:\\school\\schoollist\\baiduschool1')
    for linest in file1:
        try:
            kkqq(linest)
        except Exception:
            time.sleep(10)
            file3=file('E:\\school\\schoollist\\baiduschool-excep','a+')
            file3.write(linest)
            file3.close()




if __name__=='__main__':
    getinfo()