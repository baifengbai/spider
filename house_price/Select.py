# -*- coding: utf-8 -*
import mysql.connector
import pymysql
import repr
import sys
import chardet
reload(sys)
sys.setdefaultencoding("utf-8")
conne=mysql.connector.connect(user='root', password='123456', database='hfhouse',use_unicode=True)
cursor1=conne.cursor()
cursor1.execute("SELECT * from hfhouseprice3 WHERE name=\""+"加侨小刚PLUS\"")
rows = cursor1.fetchall()
for row in rows:
    print row
    print str(row).decode("ascii")
    print str(row).decode("ascii").encode("utf-8")
    print unicode("加侨小刚PLUS","utf-8")


    #print repr(str(row))
conn = pymysql.connect(host='localhost',port=3306,user='root',password='123456',db='hfhouse',charset='utf8')
cursor = conn.cursor()
cursor.execute("SELECT * from hfhouseprice3 WHERE name=\""+"加侨小刚PLUS\"")
rows = cursor.fetchall()
for row in rows:
    print row

