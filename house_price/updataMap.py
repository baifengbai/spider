import pymysql
import sys
import repr
reload(sys)
sys.setdefaultencoding('utf8')
conne=pymysql.connect(user='root', password='123456', database='hfhouse',use_unicode=True)
cursor1=conne.cursor()
file1=open("E:\\hfhouse\\0702\\housemap_end1.txt")
for line in file1:
    name=line.split("*")[0]
    map=line.split("*")[1]+","+line.split("*")[2]
    print map+name
    sql1 = "update hfhouseprice set map=\"" + map + "\" where name=\"" + name + "\""
    print sql1
    cursor1.execute(sql1)
    conne.commit()

file1.close()
cursor1.close()
conne.close()
