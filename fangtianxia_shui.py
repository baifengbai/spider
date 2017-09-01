# -*- coding: utf-8 -*
import sys
import string
import chardet
reload(sys)
sys.setdefaultencoding("utf-8")
'''
fangtianxia=open("E:\\hfhouse\\fangtianxia_all")
for line in fangtianxia:
    data=line.split("*")
    print data.__len__()
    if data[2]=="待定":
        continue
    if data[2]=="":
        continue
    if "均价约" in data[2]:
        data[2]=data[2].split("均价约")[1]
    if "元/平方米"in data[2]:
        data[2]=data[2].split("元/平方米")[0]
    f = file('E:\\hfhouse\\fangtianxia_all1', 'a+')
    f.write(data[0]+"*"+data[1]+"*"+data[2]+"*"+data[3]+"*"+data[4]+"*"+data[5]+"*"+data[6]+"*"+data[7]+"*"+data[8]+"*"+data[9]+"*"+data[10]+"*"+data[11]+"*"+data[12]+"*"+data[13]+"*"+data[14])
    f.close()
'''
fangtianxia_1=open('E:\\hfhouse\\fangtianxia_all1')
for line1 in fangtianxia_1:
    data=line1.split("*")
    try:
        ts = string.atoi(data[2])
    except Exception:
        print data[2]
