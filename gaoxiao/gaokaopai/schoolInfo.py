# -*- coding: utf-8 -*
#　作废
import pycurl
import StringIO
import certifi
import time
file1=file("E:\\school\\schoolname.txt")
for line in file1:
    name=line.split("\t")[1].replace("\n",'')
    url=line.split("\t")[0].replace("\n",'')
    #print url
    print repr(url)
    c = pycurl.Curl()
    c.setopt(pycurl.CAINFO, certifi.where())
    c.setopt(c.URL, url)
    b = StringIO.StringIO()
    c.setopt(pycurl.WRITEFUNCTION, b.write)
    c.perform()
    pic = b.getvalue()
    fp = open("E:\\school\\"+name, 'wb')
    fp.write(pic)
    fp.close()
    time.sleep(0.4)