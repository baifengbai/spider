# -*- coding: utf-8 -*
# 作废
import pymysql
import chardet
import sys
import repr
reload(sys)
sys.setdefaultencoding('utf8')
conn = pymysql.connect(host='localhost',port=3306,user='root',password='123456',db='gaokao',charset='utf8')
cursor = conn.cursor()
sql="INSERT INTO temp(ttt) VALUES(%s)"
file1=open("C:\\Users\\Administrator\\Desktop\\ttt.txt")
for line in file1:
    #linet=line.split("\t")
    print line
    try:
        cursor.execute(sql, (line.replace("\n", '')))
        conn.commit()
    except Exception:
        print 'ok'


cursor.close()
conn.close()