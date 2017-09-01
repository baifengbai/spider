# -*- coding: utf-8 -*
import requests
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
file1=open("E:\\hfhouse\\housename")
i=0
j=0
k=0
for line in file1:
    print line.replace("\n",'')
    url = "http://api.map.baidu.com/geocoder/v2/?ak=ptkL5uenat2I7t9PtWv8m1YhdGtNifGs&callback=renderOption&output=json&address=" + "合肥市"+line
    data = requests.get(url)
    print data.text
    #precise=1
    if "无相关结果" in data.text:
        k=k+1
        url1="http://api.map.baidu.com/geocoder/v2/?ak=ptkL5uenat2I7t9PtWv8m1YhdGtNifGs&callback=renderOption&output=json&address=" ++line
        data = requests.get(url1)
    if "无相关结果" in data.text:
        continue
    print data.text

    precise=data.text.split("{")[3].split("}")[1].split(",")[1].split(":")[1]
    print precise
    if precise=="1":
        i=i+1
    elif precise=="0":
        j=j+1

print "i:"+str(i)
print "j:"+str(j)
print "k:"+str(k)

