# -*- coding: utf-8 -*
import pymysql
import chardet
import sys
import repr
reload(sys)
sys.setdefaultencoding('utf8')
conn = pymysql.connect(host='localhost',port=3306,user='root',password='123456',db='hfhouse',charset='utf8')
cursor = conn.cursor()
sql="INSERT INTO hfhouseprice3(name,nickname,price,address,propertyType,area,loopP,developer,mainUnit,school,voRatio,greenRatio,totalHouse,propertyFee,propertyCompany,map) VALUES(%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s )"
file1=open("E:\\hfhouse\\xafc")
for line in file1:
    data=line.split("*")
    print data.__len__()
    if "一房一价" in data[1]:
        print "一房一价"
        continue
    elif "待定"==str(data[1]):
        print "待定"
        continue
    elif ""==str(data[1]):
        print "na"
        continue
    else:
        try:
            cursor.execute(sql, (data[0],"",data[1],data[2].split("】")[2],data[3],"","",data[4],data[5],data[6],data[7],data[8],"",data[9],data[10],""))
            conn.commit()
        except Exception:
            f = file('E:\\hfhouse\\xafc_same', 'a+')
            new_content =line + "\n"
            f.write(new_content)
            f.close()

    #cursor.execute(sql, ())
    #conn.commit()


cursor.close()
conn.close()