# -*- coding: utf-8 -*
import sys
import string
import chardet
import requests
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding("utf-8")
ipath="C:\\Users\\Administrator\\Desktop\\小学\\\屯溪路小学\\滨湖.txt"
path=unicode(ipath,'utf-8')
file1=open(path)
i=0
j=0
for line in file1:
    data=line.split('*')[1]
    i=i+float(data)
    j=j+1
print i
print j
p1=i/j
print p1
file1.close()
print '-----------------------------------------------'
ipath1="C:\\Users\\Administrator\\Desktop\\小学\\\屯溪路小学\\金斗路.txt"
path1=unicode(ipath1,'utf-8')
file2=open(path1)
i=0
j=0
for line in file2:
    data=line.split('*')[1]
    i=i+float(data)
    j=j+1
print i
print j
p1=i/j
print p1
file2.close()

print '-----------------------------------------------'
ipath2="C:\\Users\\Administrator\\Desktop\\小学\\\屯溪路小学\\阳光小学.txt"
path2=unicode(ipath2,'utf-8')
file3=open(path2)
i=0
j=0
for line in file3:
    data=line.split('*')[1]
    i=i+float(data)
    j=j+1
print i
print j
p1=i/j
print p1
file3.close()