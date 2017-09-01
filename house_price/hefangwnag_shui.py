# -*- coding: utf-8 -*
import sys
import string
import chardet
reload(sys)
sys.setdefaultencoding("utf-8")
'''
hefangwang=open("E:\\hfhouse\\hefangwang")
for line in hefangwang:
    data=line.split("*")
    print data.__len__()
    if data[1]=="一房一价":
        continue
    if data[1]=="待定":
        continue
    if data[1]=="":
        continue
    if "元/" in data[1]:
        data[1]=data[1].split("元/")[0]
    f = file('E:\\hfhouse\\hefangwang_1', 'a+')
    f.write(data[0]+"*"+data[1]+"*"+data[2]+"*"+data[3]+"*"+data[4]+"*"+data[5]+"*"+data[6]+"*"+data[7]+"*"+data[8]+"*"+data[9]+"*"+data[10]+"*"+data[11]+"*"+data[12])
    f.close()
'''
hefangwang_1=open('E:\\hfhouse\\hefangwang_1')
for line1 in hefangwang_1:
    data=line1.split("*")
    try:
        ts = string.atoi(data[1])
    except Exception:
        print data[1]
