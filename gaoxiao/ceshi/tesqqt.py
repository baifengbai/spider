# -*- coding: UTF-8 -*-
# 才储 28提
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import urllib
import urllib2
values = {}
values['feishi']="3690"
values['id']=""
values['sex']="famale"
values['nianling']="00"
values['tishu']="28"
values['email']=""
values['answer1']="0"
values['answer2']="0"
values['answer3']="1"
values['answer4']="1"
values['answer5']="0"
values['answer6']="0"
values['answer7']="1"
values['answer8']="0"
values['answer9']="1"
values['answer10']="1"
values['answer11']="1"
values['answer12']="1"
values['answer13']="0"
values['answer14']="0"
values['answer15']="1"
values['answer16']="1"
values['answer17']="0"
values['answer18']="1"
values['answer19']="1"
values['answer20']="1"
values['answer21']="0"
values['answer22']="1"
values['answer23']="0"
values['answer24']="0"
values['answer25']="1"
values['answer26']="1"
values['answer27']="0"
values['answer28']="1"
#values = {feishi,id,sex,nianling,tishu,email,answer1,answer2,answer3,answer4,answer5,answer6,answer7,answer8,answer9,answer10,answer11,answer12,answer13,answer14,answer15,answer16,answer17,answer18,answer19,answer20,answer21,answer22,answer23,answer24,answer25,answer26,answer27,answer28}
data = urllib.urlencode(values)
url = "http://www.apesk.com/mbti/submit_dtwz_jk_2014_psy.asp"
#url="http://www.apesk.com/mbti/dati.asp"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36",'Referer':"http://www.apesk.com/mbti/dati.asp"}
request = urllib2.Request(url, data,headers)
response = urllib2.urlopen(request)
print response.read()