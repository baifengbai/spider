# -*- coding: utf-8 -*
import requests
from bs4 import BeautifulSoup
import sys
import repr
reload(sys)
sys.setdefaultencoding('utf8')

#url="http://365jia.cn/news/2017-06-07/A527916447480261.html"#蜀山小学
#url1="http://365jia.cn/news/2017-06-07/0D5A851E15ED70F6.html"#蜀山中心
#url2='http://365jia.cn/news/2017-06-07/AE24FBADFA3202AF.html'#庐阳小学
url3='http://365jia.cn/news/2017-06-07/BE8BB3ADC276279D.html'#庐阳中学
data=requests.get(url3).text
bsoup=BeautifulSoup(data,"lxml")
data=bsoup.select(" div > p")
for line in data:
    if "." in str(line.get_text()):
        print line.get_text().split(".")[1]

        name = line.get_text().split(".")[1]
        line.get_text()
        f = file('E:\\hfschool\\middle2', 'a+')
        new_content = name + "*安徽省*合肥市*庐阳区""\n"
        f.write(new_content)
        f.close()

