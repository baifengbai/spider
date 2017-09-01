# -*- coding: utf-8 -*
from bs4 import BeautifulSoup
import lxml
import re

import StringIO
import sys

reload(sys)
sys.setdefaultencoding('utf8')
path="E:\\gaokao\\北京2017.xlsx"
ipath=unicode(path,'utf-8')
file1=open(ipath)
for line in file1:
    print line