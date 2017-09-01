# -*- coding: utf-8 -*
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
file1=open('E:\\new_12761_20170621.csv')
yaohai=0
xinzhan=0
shusan=0
shixia=0
luyang=0
baohe=0
jingkai=0
gaoxin=0
for line in file1:
    if "合肥市" in line:
        if "瑶海" in line:
            print line
            yaohai=yaohai+1
        elif "新站试验" in line:
            print line
            xinzhan=xinzhan+1
        elif "市辖" in line:
            print line
            shixia=shixia+1
        elif "蜀山"  in line:
            print line
            shusan=shusan+1
        elif "庐阳" in line:
            print line
            luyang=luyang+1
        elif "包河" in line:
            print line
            baohe=baohe+1
        elif "经济开发" in line:
            print line
            jingkai=jingkai+1
        elif "高新开发" in line:
            print line
            gaoxin=gaoxin+1
print "瑶海"+str(yaohai)
print "新站实验"+str(xinzhan)
print "市辖"+str(shixia)
print "蜀山" +str(shusan)
print "庐阳"+str(luyang)
print "包河"+str(baohe)
print "经济开发"+str(jingkai)
print "高新开发"+str(gaoxin)