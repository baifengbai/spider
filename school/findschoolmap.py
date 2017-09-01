# -*- coding: utf-8 -*
import requests
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
file1=open("E:\\hfschool\\nanachi.txt")
i=0
j=0
k=0
for line in file1:



    url = "http://api.map.baidu.com/geocoder/v2/?ak=ptkL5uenat2I7t9PtWv8m1YhdGtNifGs&callback=renderOption&output=json&address=" + "合肥市" + line.replace("\n",'').split("*")[0]

    print url
    data = requests.get(url)
    precise = data.text.split("{")[3].split("}")[1].split(",")[1].split(":")[1]
    print data.text
    if precise==str(0):
        print line.replace("\n", '')
        print data.text
        f = file('E:\\hfschool\\excep', 'a+')
        f.write(line.replace("\n",'')+data.text+"\n")
        f.close()
    elif precise==str(1):
        lng=str(data.text).split("{")[3].split("}")[0].split(",")[0].split(":")[1]
        lat=str(data.text).split("{")[3].split("}")[0].split(",")[1].split(":")[1]
        f = file('E:\\hfschool\\nanachimap', 'a+')
        f.write(line.replace("\n", '') + "*"+lng+"*"+lat+"*1"+"\n")
        f.close()

