# -*- coding: utf-8 -*
import sys
import string
import chardet
import requests
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding("utf-8")
ipath="C:\\Users\\Administrator\\Desktop\\初中\\合肥市第四十五中学（工业园分校）.txt"
path=unicode(ipath,'utf-8')
file1=open(path)
i=0
j=0