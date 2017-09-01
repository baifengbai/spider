# -*- coding: utf-8 -*
#将中小学名单倒入到数据库
import pymysql
import sys
import repr
reload(sys)
sys.setdefaultencoding('utf8')
conn = pymysql.connect(host='localhost',port=3306,user='root',password='123456',db='hfhouse',charset='utf8')
cursor = conn.cursor()
sql="INSERT INTO schooltempP(name,score) VALUES(%s, %s)"
#file=open("E:\\hfschool\\primarymap.txt")
file=open("E:\\hfschool\\zhongdianmid")
for line in file:
    data=line.split("*")
    print data.__len__()
    #cursor.execute(sql, (data[0],data[1],data[2],data[3],"1"))# 1 primary
    try:
        cursor.execute(sql, (data[0], float(data[1]))) # 2 middle
        conn.commit()
    except Exception:
        print sql
    #cursor.execute(sql, ())
    #conn.commit()
file.close()
cursor.close()
conn.close()