# -*- coding: utf-8 -*
# 名单
import urllib2
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
url = 'https://www.wmzy.com/api/school/getSchList?prov_filter=00&type_filter=0&diploma_filter=0&flag_filter=0&page=1&page_len=3000&_=150183567867867'
request=urllib2.Request(url)
response = urllib2.urlopen(request)
hf=response.read()
soup=BeautifulSoup(hf[12:-2],'lxml')
lines=soup.select(" h3 > a ")
print lines.__len__()
file1=file("schoollist",'a+')
for line in lines:
    name=line.get_text().replace("\n",'').replace(" ",'').replace(r"\n",'')
    print name
    href=str(line.get('href')).replace(r"\"",'')
    print href
    #new_n=str(name)+str("*")+str(href)+str("\n")
    file1.write(name)
    file1.write("*")
    file1.write(href)
    file1.write("\n")
file1.close()