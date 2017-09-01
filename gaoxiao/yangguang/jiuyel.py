# -*- coding: utf-8 -*
# 忽略
import time
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


file_2 = file("E:\\school\\yangguanggaokao\\zhuanye\\z1", 'a+')
file_3 = file("E:\\school\\yangguanggaokao\\zhuanye\\ye", 'a+')
for line in file_2:
    temp = line.split("*")
    name = temp[0]
    file_3.write(name)
    file_3.write("*")
    jiuye_all = temp[1]
    temp_2 = jiuye_all.split(")")
    jiuye_2014 = temp_2[0].split("(")
    jiuye_2015 = temp_2[1].split("(")
    jiuye_2016 = temp_2[2].split("(")
    file_3.write(jiuye_2014[1]+"*"+jiuye_2015[1]+"*"+jiuye_2016[1]+"\n")
file_3.close()
file_2.close()
