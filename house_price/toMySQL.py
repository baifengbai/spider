# -*- coding: utf-8 -*
import pymysql
import sys
import repr
reload(sys)
sys.setdefaultencoding('utf8')
conn = pymysql.connect(host='localhost',port=3306,user='root',password='123456',db='hfhouse',charset='utf8')
cursor = conn.cursor()
sql="INSERT INTO hfhouseprice1(name,nickname,price,address,propertyType,area,loopP,developer,mainUnit,school,voRatio,greenRatio,totalHouse,propertyFee,propertyCompany,map) VALUES(%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s )"
file=open("E:\\hfhouse\\xafc")
for line in file:
    data=line.split("*")
    print data.__len__()
    if "一房一价" in data[1]:
        print "一房一价"
        continue
    elif "待定"==str(data[1]):
        print "待定"
        continue
    else:
        cursor.execute(sql, (data[0],"",data[1],data[2],data[3],data[4],"","",data[5],data[6],data[7],data[8],"",data[9],data[10],""))
        conn.commit()

    #cursor.execute(sql, ())
    #conn.commit()


cursor.close()
conn.close()