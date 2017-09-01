import urllib2
import json
import time
import pymysql


def main():
    url = "http://www.xdaili.cn/ipagent//greatRecharge/getGreatIp?spiderId=9da3a75c587e46a9b8039eaa91f3ea9c&orderno=MF20178217365FsU5IA&returnType=2&count=20"
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    hd = response.read()
    # print hd
    json_h = json.loads(hd)
    conn = pymysql.connect(host='172.31.8.10', port=3306, user='jiezhang',
                           password='jiezhang', db='zhiyuan', charset='utf8')
    cursor = conn.cursor()
    sql = "INSERT INTO IPproxy2(host,port,grade) VALUES(%s, %s, %s)"
    for line in json_h['RESULT']:
        port = line['port']
        ip = line['ip']
        try:
            cursor.execute(sql, (ip, port, 20))
            conn.commit()
        except:
            pass
    cursor.close()
    conn.close()


if __name__ == "__main__":
    while(True):
        main()
        time.sleep(30)
