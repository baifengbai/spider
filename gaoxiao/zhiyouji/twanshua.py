# -*- coding: utf-8 -*
# 忽略
from bs4 import BeautifulSoup
import urllib
import urllib2
import cookielib
import sys
reload(sys)
sys.setdefaultencoding('utf8')

url='http://www.jobui.com/trends/%E5%85%A8%E5%9B%BD-%E9%94%80%E5%94%AE%E7%BB%8F%E7%90%86/'
request = urllib2.Request(url)
response = urllib2.urlopen(request)
hdd=response.read()
print hdd
soup=BeautifulSoup(hdd,'lxml')
lines=soup.select(" ol > li > span > span.barlist-title > a ")
print lines.__len__()
lines2=soup.select(" ol > li > span > span.barlist-value > a ")
print lines2.__len__()
lines3=soup.select(" ol > li > span > span.barlist-value > em ")
print lines3.__len__()

url='http://www.jobui.com/salary/%E5%85%A8%E5%9B%BD-%E9%94%80%E5%94%AE%E7%BB%8F%E7%90%86/'
request = urllib2.Request(url)
response = urllib2.urlopen(request)
hdd=response.read()
print hdd
soup=BeautifulSoup(hdd,'lxml')
lines4=soup.select(" ul.statistics-numbox > li > span.section-val ")
print lines4.__len__()
lines5=soup.select(" ul.statistics-numbox > li > span.specific-val ")
print lines5.__len__()
lines6=soup.select(" div.credible > h3.salary-avger ")
print lines6.__len__()