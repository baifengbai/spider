# -*- coding: utf-8 -*
from __future__ import unicode_literals

import requests
import sys
import json
import urllib
import urllib2


reload(sys)
sys.setdefaultencoding("utf-8")
file1=open("E:\\hfschool\\excep")
for line in file1:
    print line.split("*")[0]
    url="http://api.map.baidu.com/?qt=s&c=127&wd="+line.split("*")[0]+"&rn=10&ie=utf-8&oue=1&fromproduct=jsapi&res=api&callback=BMap._rd._cbk94732&ak=E4805d16520de693a3fe707cdc962045"
    data = requests.get(url).text
    print data
    jqq = data[45:-1]
    print jqq
    if 'content' in str(jqq):
        hjson = json.loads(jqq)
        x=str(hjson['content']).split("diPointX")[1].split(',')[0].split(":")[1]
        print x
        y=str(hjson['content']).split("diPointY")[1].split(',')[0].split(":")[
            1]
        print y
        if x!="0":
            values = {}
            values['mctX'] = x
            values['mctY'] = y


