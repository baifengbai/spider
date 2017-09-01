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
sql="INSERT INTO provinceGrade(province,batch,studenttype,grade,year) VALUES(%s, %s,%s,%s,%s)"
file1=open("E:\\school\\schoolprovince\\grade")
for line in file1:
    data=line.split("*")
    print data.__len__()
    try:
        cursor.execute(sql, (data[0],data[1],data[2],data[3],data[4].replace("\n",'')))
        conn.commit()
    except Exception:
        f = file('E:\\school\\schoolprovince\\grade_excet', 'a+')
        new_content =line + "\n"
        f.write(new_content)
        f.close()

    #cursor.execute(sql, ())
    #conn.commit()
cursor.close()
conn.close()