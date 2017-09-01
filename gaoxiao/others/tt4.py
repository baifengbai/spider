# -*- coding: utf-8 -*
"""test dfgdfsgsikdjfhawkj"""
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


file_2 = file("C:\\Users\\Administrator\\Desktop\\tt2.txt")
i = 1
t_0 = 0
for lines in file_2:

    temp_2 = lines.split("\t")
    try:
        if int(temp_2[2]) == int(temp_2[1]) + t_0:
            t_0 = int(temp_2[2])
            pass
        else:
            print i
            print lines
            break
    except:
        print i
        print lines

    i += 1
file_2.close()
