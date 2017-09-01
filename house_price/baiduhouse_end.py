# -*- coding: utf-8 -*
from __future__ import unicode_literals

import requests
import sys
import json
import urllib
import urllib2


reload(sys)
sys.setdefaultencoding("utf-8")
file1=open("E:\\hfhouse\\0702\\mapnull2")
for line in file1:
    #print line.split("*")[0]
    url="http://api.map.baidu.com/?qt=s&c=127&wd="+'合肥市'+line.replace("\n",'')+"&rn=10&ie=utf-8&oue=1&fromproduct=jsapi&res=api&callback=BMap._rd._cbk94732&ak=E4805d16520de693a3fe707cdc962045"
    data = requests.get(url).text
    #print data
    jqq = data[45:-1]
    #print jqq
    if 'content' in str(jqq):
        hjson = json.loads(jqq)
        try:
            x=str(hjson['content']).split("diPointX")[1].split(',')[0].split(":")[1]
            print x
            y=str(hjson['content']).split("diPointY")[1].split(',')[0].split(":")[1]
            print y
            f1=file("E:\\hfhouse\\0702\\mapnullmap.txt",'a+')
            new_count=line.replace("\n",'')+"*"+x+"*"+y+"\n"
            f1.write(new_count)
            f1.close()
        except Exception:
            f2 = file("E:\\hfhouse\\0702\\mapnull_excep.txt", 'a+')
            new_count = line
            f2.write(new_count)
            f2.close()
    else:
        print "can't find the "+line.split("*")[0]
        f3=file("E:\\hfhouse\\0702\\mapnull_excep.txt",'a+')
        new_count=line
        f3.write(new_count)
        f3.close()


