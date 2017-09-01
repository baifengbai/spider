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
sql="INSERT INTO provinceGrade(year,province,studenttype,batch,grade) VALUES(%s, %s,%s,%s,%s)"
file1=open("E:\\school\\schoolprovince\\gaokaopaigrade")
for line in file1:
    data=line.split("*")
    d0=data[0]
    d1=data[1]
    d2=data[2]
    d3=data[3]
    d4=data[4].replace("\n",'')
    print data.__len__()
    try:
        cursor.execute(sql, (d0,d1,d2,d3,d4))
        conn.commit()
    except Exception:
        sql1="SELECT grade from provinceGrade WHERE year="+d0+" and province=\'"+d1+"\' and studenttype=\'"+d2+"\' and batch=\'"+d3+"\'"
        print sql1
        cursor.execute(sql1)
        rows = cursor.fetchall()
        for row in rows:
            if int(str(d4))==int(row[0]):
                print "ok"
            else :
                print line
                f = file('E:\\school\\schoolprovince\\grade_excet', 'a+')
                new_content = line + "\n"
                f.write(new_content)
                f.close()

    #cursor.execute(sql, ())
    #conn.commit()
cursor.close()
conn.close()