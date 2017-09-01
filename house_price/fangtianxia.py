# -*- coding: utf-8 -*
import urllib
import urllib2
from bs4 import BeautifulSoup
import lxml

url1="http://newhouse.hf.fang.com/house/s/?ctm=1.hf.xf_search.lpsearch_area.1"#fang tian xia
url2="https://hf.fang.anjuke.com/loupan/?pi=baidu-cpcaf-hf-tyonghf1&utm_source=baidu&utm_medium=cpc&kwid=40307903159&utm_term=%E6%88%BF%E6%BA%90%E7%BD%91"#an ke ju
response = urllib2.urlopen(url2)
#print response.read()
html=response.read()
soup=BeautifulSoup(html)
print soup.prettify(formatter=html)