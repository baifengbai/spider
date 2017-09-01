# -*- coding: utf-8 -*
# 百度学校名单
import time
import urllib
import urllib2
import json
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def school(i):
    values = {}
    values['limit'] = "30"
    values['timeout'] = "3000"
    values['filterTags'] = "%5B0%2C0%2C0%2C0%2C0%2C0%2C0%5"
    values['tagId'] = "60829"
    values['fromLemma'] = "false"
    values['contentLength'] = "40"
    values['page'] = str(i)
    data = urllib.urlencode(values)
    url1 = "https://baike.baidu.com/wikitag/api/getlemmas"

    # url="http://www.apesk.com/mbti/dati.asp"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36",
        'Referer': "https://baike.baidu.com/wikitag/taglist?tagId=60829"}
    request = urllib2.Request(url1, data, headers)
    response = urllib2.urlopen(request)
    # print response.read()
    hd = response.read()
    hjson = json.loads(str(hd))
    i = 0
    file1=file('E:\\school\\schoollist\\baiduschool','a+')
    for school in hjson['lemmaList']:
        name = school['lemmaTitle']
        print name
        uu = school['lemmaUrl']
        print uu
        file1.write(str(name)+'*'+str(uu)+'\n')
    file1.close()




if __name__=="__main__":
    i=0
    while i < 81:
        school(i)
        i+=1