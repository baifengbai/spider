# -*- coding: utf-8 -*
import sys
import string
import chardet
reload(sys)
sys.setdefaultencoding("utf-8")

anjuke=open("E:\\hfhouse\\anjuke_zhengwuqu")
for line in anjuke:
    data=line.split("*")
    print data.__len__()
    if(data.__len__()==17):
        print data


    if data[2]=="":
        continue
    if "待定" in data[2]:
        continue
    f = file('E:\\hfhouse\\anjuke_zhengwuqu1', 'a+')
    f.write(line)
    f.close()

anjuke_1=open('E:\\hfhouse\\anjuke_zhengwuqu1')
for line1 in anjuke_1:
    data=line1.split("*")
    try:
        ts = string.atoi(data[2])
    except Exception:
        print data[2]