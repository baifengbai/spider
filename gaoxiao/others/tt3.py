# -*- coding: utf-8 -*
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


file_2 = file("C:\\Users\\Administrator\\Desktop\\tt2.txt")
i = 1
for lines in file_2:

    temp_2 = lines.split("\t")
    try:
        for temp in temp_2:
            #print temp
            int(temp)
    except:
        print i
        print lines

    i += 1
file_2.close()
