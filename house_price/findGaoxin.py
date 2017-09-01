# -*- coding: utf-8 -*
import requests
from bs4 import BeautifulSoup
import sys
import repr
reload(sys)
sys.setdefaultencoding('utf8')
#url3='http://news.hf365.com/system/2017/06/07/015300388_05.shtml'
#url4='http://news.hf365.com/system/2017/06/07/015300388_04.shtml'
#url5='http://hf.aoshu.com/e/20170605/5934c950f1b49.shtml'
url6='http://www.jianbihua.cc/zixun/jiaoyu/2034.html'
data=requests.get(url6)
data.encoding = "gb2312"
data=data.text
bsoup=BeautifulSoup(data,"lxml")
data=bsoup.select(" p ")
for line in data:
    if "、" in str(line):
        print line.get_text().strip().replace("\r\n",'').split("、")[1].split("：")[0]
        name=line.get_text().strip().replace("\r\n",'').split("、")[1].split("：")[0]
        #print repr(str(name))
        f = file('E:\\hfschool\\baohe_pri', 'a+')
        new_content = name + "*安徽省*合肥市*包河区""\n"
        f.write(new_content)
        f.close()


