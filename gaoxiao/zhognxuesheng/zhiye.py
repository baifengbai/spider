# -*- coding: utf-8 -*

import pycurl
import certifi
import StringIO
import urllib2
import json
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf8')



def getzz(id):
    # get majorName
    url1='http://www.stu-career.com/divisionCenter/getMajorInfoById.action?id='+str(id)+'&date=Mon+Jul+31+2017+15%3A22%3A29+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&_=1501485749946'
    try:
        request1 = urllib2.Request(url1)
        response1 = urllib2.urlopen(request1)
    except Exception:
        request1 = urllib2.Request(url1)
        response1 = urllib2.urlopen(request1)
    hdd = response1.read()
    print hdd
    try:
        hjs=json.loads(hdd)
    except Exception:
        return
    istrue=hjs['message']
    if istrue=='true':
        majorName = hjs['majorName']
        print majorName
        # get major zhiye
        url = 'http://www.stu-career.com/divisionCenter/findVocation.action?id=' + str(
            id) + '&date=Mon+Jul+31+2017+15%3A07%3A14+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&page=0&_=1501484834546'
        try:
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
        except Exception:
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
        hd = response.read()
        print hd
        mjs = json.loads(hd)
        total = mjs['total']
        if total != 0:
            new_n = majorName
            for data in mjs['datas']:
                new_n = new_n + "*" + str(data['name']).replace("\n", '')
            j = 1
            while j < int(mjs['totalPage']):
                url2 = 'http://www.stu-career.com/divisionCenter/findVocation.action?id=' + str(
                    id) + '&date=Mon+Jul+31+2017+15%3A07%3A14+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&page=' + str(
                    j) + '&_=1501484834546'
                try:
                    request2 = urllib2.Request(url2)
                    response2 = urllib2.urlopen(request2)
                except Exception:
                    request2 = urllib2.Request(url2)
                    response2 = urllib2.urlopen(request2)
                hdt = response2.read()
                print hdt
                xjs = json.loads(hdt)
                for dataq in xjs['datas']:
                    new_n = new_n + "*" + str(dataq['name']).replace("\n", '')
                j += 1
            file1 = file('E:\\school\\yangguanggaokao\\zhongxuesheng', 'a+')
            file1.write(new_n + '\n')
            file1.close()



if __name__=='__main__':
    i=1
    while i < 1627:
        print "i:"+str(i)
        getzz(i)
        i+=1