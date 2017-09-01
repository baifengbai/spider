# -*- coding: utf-8 -*
import sys
import urllib2
import socket

reload(sys)
sys.setdefaultencoding('utf8')


class getIP():
    def getIPlist(self):
        socket.setdefaulttimeout(3)
        f = open("E:\\IP\\proxy")
        lines = f.readlines()
        proxys = []
        list = []
        for i in range(0, len(lines)):
            ip = lines[i].strip("\n").split("\t")
            proxy_host = "http://" + ip[0] + ":" + ip[1]
            proxy_temp = {"http": proxy_host}
            proxys.append(proxy_temp)
        url = "http://ip.chinaz.com/getip.aspx"
        for proxy in proxys:
            try:
                # print proxy
                # request = urllib2.Request(url)
                try:
                    response = urllib2.urlopen(url, timeout=10)
                    # print response.getcode()
                    if response.getcode() == 200:
                        list.append(proxy)
                except Exception:
                    # print 'xx'
                    pass

            except Exception, e:
                print proxy
                print e
                continue
        return list


if __name__ == '__main__':
    list = getIP().getIPlist()
    print list
