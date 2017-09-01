# -*- coding: utf-8 -*
import ghost
from ghost import Ghost
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
g = Ghost()
url="http://www.site-digger.com/tools/mct2latlng.html"
file1=open("E:\\hfhouse\\0702\\mapnullmap.txt",'a+')
with g.start() as session:
   page, extra_resources = session.open("http://www.site-digger.com/tools/mct2latlng.html")

   for line in file1:
       x=float(line.split('*')[1])/100
       y=float(line.split('*')[2])/100
       session.set_field_value("#mctX", str(x))
       session.set_field_value("#mctY", str(y))
       session.evaluate("mctGeo()")
       lng = session.content.split('经纬度lng:')[1].split("<")[0].strip()
       lat = session.content.split('经纬度lat:')[1].split("<")[0].strip()
       print lng
       print lat
       f1 = file("E:\\hfhouse\\0702\\housemap_end1.txt", 'a+')
       data=line.split('*')
       new_count = data[0] + "*" + lng + "*" + lat + "\n"
       f1.write(new_count)
       f1.close()

file1.close()
g.exit()
