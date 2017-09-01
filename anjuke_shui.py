# -*- coding: utf-8 -*
import sys
import string
import chardet
reload(sys)
sys.setdefaultencoding("utf-8")
'''
anjuke=open("E:\\hfhouse\\anjuke")
for line in anjuke:
    data=line.split("*")
    print data.__len__()
    if data[1]=="住宅 待定":
        continue
    if data[1]=="商住 待定":
        continue
    if data[1]=="写字楼 待定":
        continue
    if data[1]=="":
        continue
    if "住宅" in data[1]:
        data[1]=data[1].split("住宅")[1]
    if "元/"in data[1]:
        data[1]=data[1].split("元/")[0]
    if "商铺" in data[1]:
        data[1]=data[1].split("商铺")[1]
    if "写字楼" in data[1]:
        data[1]=data[1].split("写字楼")[1]
    if "商住" in data[1]:
        data[1]=data[1].split("商住")[1]
    if "别墅" in data[1]:
        data[1] = data[1].split("别墅")[1]
    if "待定" in data[1]:
        continue
    f = file('E:\\hfhouse\\anjuke_1', 'a+')
    f.write(data[0]+"*"+data[1]+"*"+data[2]+"*"+data[3]+"*"+data[4]+"*"+data[5]+"*"+data[6]+"*"+data[7]+"*"+data[8]+"*"+data[9]+"*"+data[10]+"*"+data[11]+"*"+data[12])
    f.close()
'''
anjuke_1=open('E:\\hfhouse\\anjuke_1')
for line1 in anjuke_1:
    data=line1.split("*")
    try:
        ts = string.atoi(data[1])
    except Exception:
        print data[1]
