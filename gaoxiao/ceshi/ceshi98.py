# -*- coding: UTF-8 -*-
# 才储93题
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import urllib
import urllib2
import re


values = {}
values['feishi']="3690"
values["hr_email"] = ""
values['sex']="famale"
values['tishu']="93"
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
values['answer29']="0"
values['answer30']="0"
values['answer31']="1"
values['answer32']="1"
values['answer33']="0"
values['answer34']="0"
values['answer35']="1"
values['answer36']="0"
values['answer37']="1"
values['answer38']="1"
values['answer38']="1"
values['answer39']="1"
values['answer40']="0"
values['answer41']="0"
values['answer42']="1"
values['answer43']="1"
values['answer44']="0"
values['answer45']="1"
values['answer46']="1"
values['answer47']="1"
values['answer48']="0"
values['answer49']="1"
values['answer50']="0"
values['answer51']="0"
values['answer52']="1"
values['answer53']="1"
values['answer54']="0"
values['answer55']="1"
values['answer56']="1"
values['answer57']="1"
values['answer58']="0"
values['answer59']="0"
values['answer60']="1"
values['answer61']="1"
values['answer62']="0"
values['answer63']="1"
values['answer64']="1"
values['answer65']="1"
values['answer66']="0"
values['answer67']="1"
values['answer68']="0"
values['answer69']="0"
values['answer70']="1"
values['answer71']="1"
values['answer72']="0"
values['answer73']="1"
values['answer74']="0"
values['answer74']="0"
values['answer76']="1"
values['answer77']="1"
values['answer78']="0"
values['answer79']="0"
values['answer80']="1"
values['answer81']="0"
values['answer82']="1"
values['answer83']="1"
values['answer84']="1"
values['answer85']="1"
values['answer86']="0"
values['answer87']="0"
values['answer88']="1"
values['answer89']="1"
values['answer90']="0"
values['answer91']="1"
values['answer92']="1"
values['answer93']="0"
#values = {feishi,id,sex,nianling,tishu,email,answer1,answer2,answer3,answer4,answer5,answer6,answer7,answer8,answer9,answer10,answer11,answer12,answer13,answer14,answer15,answer16,answer17,answer18,answer19,answer20,answer21,answer22,answer23,answer24,answer25,answer26,answer27,answer28}
data = urllib.urlencode(values)
url = "http://www.apesk.com/mbti/submit_dtwz_jk_zy.asp"
#url="http://www.apesk.com/mbti/dati.asp"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36",'Referer':"http://www.apesk.com/mbti/dati.asp"}
request = urllib2.Request(url, data,headers)
response = urllib2.urlopen(request)
#print response.read()
hd = response.read()
print str(hd[:-200]).decode("gb2312")
hf = hd + "</body >"
soup = BeautifulSoup(hd, 'lxml')
lines = soup.findAll(class_="green button")
print lines.__len__()
for line in lines:
    if "/mbti/submit_email_date_zy.asp?code" in line.get("href"):
        print "http://www.apesk.com"+line.get("href")
