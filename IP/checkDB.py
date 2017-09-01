# -*- coding: utf-8 -*
# IP池管理相关
import sys
import getIP66
import pymysql
import getIPxici
import getIPxdai
import getIP89ip
import time
reload(sys)
sys.setdefaultencoding("utf-8")


def delete_ip():
    conn = pymysql.connect(host='172.31.8.10', port=3306, user='jiezhang',
                           password='jiezhang', db='zhiyuan', charset='utf8')
    cursor = conn.cursor()
    sql_2 = "DELETE FROM IPproxy where grade < -2 "
    cursor.execute(sql_2)
    conn.commit()
    cursor.close()
    conn.cursor()


def main():
    list1 = []
    list2 = []
    list1 = getIP66.getIPs()
    list2 = getIPxici.getxici()
    list3 = getIPxdai.getIPs()
    list4 = getIP89ip.getIPs()
    list1.extend(list2)
    list1.extend(list3)
    list1.extend(list4)

    conn = pymysql.connect(host='172.31.8.10', port=3306, user='jiezhang',
                           password='jiezhang', db='zhiyuan', charset='utf8')
    cursor = conn.cursor()
    sql = "INSERT INTO IPproxy(host,port,grade) VALUES(%s, %s, %s)"
    for lines in list1:
        try:
            cursor.execute(sql, (str(lines).split(":")[0], str(lines).split(":")[1], 0))
            conn.commit()
        except:
            pass
    sql_1 = "INSERT INTO IPproxy1(host,port,grade) VALUES(%s, %s, %s)"
    for lines in list1:
        try:
            cursor.execute(sql_1, (str(lines).split(":")[0], str(lines).split(":")[1], 2))
            conn.commit()
        except:
            pass
    cursor.close()
    conn.close()

if __name__ == '__main__':
    while True:
        print "sleeping........."
        time.sleep(1200)
        print " 干活啦"
        main()
        delete_ip()
        print "laozi 不干了"