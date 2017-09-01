# -*- coding: utf-8 -*
# 高考派的学校校徽
import pycurl
import StringIO
import certifi
import time
file1=file("E:\\schoolimage\\image.txt")
for line in file1:
    name=line.split("\t")[0]
    url=line.split("\t")[1].replace("\n",'')
    #print url
    print repr(url)
    c = pycurl.Curl()
    c.setopt(pycurl.CAINFO, certifi.where())
    c.setopt(c.URL, url)
    b = StringIO.StringIO()
    c.setopt(pycurl.WRITEFUNCTION, b.write)
    c.perform()
    pic = b.getvalue()
    fp = open("E:\\schoolimage\\"+name+".jpg", 'wb')
    fp.write(pic)
    fp.close()
    time.sleep(0.4)

#url="http://cdn.stc.gaokaopai.com/Public/Uploads/13Z01153G40-62N9.jpg"

