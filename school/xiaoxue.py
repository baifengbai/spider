# -*- coding: utf-8 -*
import requests
from bs4 import BeautifulSoup
import sys
import repr
reload(sys)
sys.setdefaultencoding('utf8')

def find(url):
    data=requests.get(url)
    data=data.text
    info=BeautifulSoup(data,'lxml')
    infodata=info.select('div.sk')
    print infodata.__len__()
    for xn in infodata:
        #print xn.get_text().rstrip()
        sb=str(xn.get_text().rstrip()).split("电话")
        print sb[0]
        sb2=str(xn.get_text().rstrip()).split("地址：")
        print sb2[1]
        #f=file('E:\\hfschool\\primary','a+')
        f = file('E:\\hfschool\\primary1', 'a+')
        new_content=sb[0]+"*"+sb2[1]+"*安徽省*合肥市*包河区""\n"
        f.write(new_content)
        f.close()



i=1
#while i<19:
while i<4:
    #url = "http://www.ruyile.com/xuexiao/?a=186&t=2&p="+str(i)#primary
    url='http://www.ruyile.com/xuexiao/?a=2225&t=2&p='+str(i)#middle
    find(url)
    i=i+1
