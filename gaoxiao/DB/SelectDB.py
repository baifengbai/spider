# -*- coding: utf-8 -*
# 作废
import pymysql
import telnetlib
from multiprocessing import Pool
import multiprocessing
#IPok = []


def tePro(lines,llst):
    #global IPok
    try:
        telnetlib.Telnet(str(lines).split(":")[0],
                         port=str(lines).split(":")[1], timeout=2)
    except:
        print 'connect failed'
        pass
    else:
        print 'success'
        llst.append(str(lines))

if __name__=="__main__":
    list = []
    conn = pymysql.connect(host='172.31.8.10', port=3306, user='jiezhang',
                           password='jiezhang', db='zhiyuan', charset='utf8')
    cursor = conn.cursor()
    sql = "SELECT * FROM IPproxy "
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        list.append(row[0] + ":" + row[1])
    print list
    mgr = multiprocessing.Manager()
    llst = mgr.list()
    pool = Pool(processes=6)
    for liness in list:
        pool.apply_async(tePro, args=(liness, llst))
    pool.close()
    pool.join()


