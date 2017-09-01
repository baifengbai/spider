# -*- coding: utf-8 -*
import urllib
import urllib2
import requests
City_Code="127"
key_word="世茂翡翠"
values={"newmap":"1","reqflag": "pcmap","biz": "1","from": "webmap","da_par": "direct",  "pcevaname": "pc4.1",  "qt": "con","c": City_Code, "wd": key_word, "wd2": "","pn": 1,
        "nn": 10,
        "db": "0",
        "sug": "0",
        "addr": "0",
        "da_src": "pcmappg.poi.page",
        "on_gel": "1",
        "src": "7",
        "gr": "3",
        "l": "12",
        "tn": "B_NORMAL_MAP",
        # "u_loc": "12621219.536556,2630747.285024",
        "ie": "utf-8",
        # "b": "(11845157.18,3047692.2;11922085.18,3073932.2)",  #这个应该是地理位置坐标，可以忽略
        "t": "1468896652886"   }
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36(KHTML, like Gecko) Chrome/56.0.2924.87Safari/537.36'}
url = 'http://map.baidu.com/'
htm = requests.get(url, params=values, headers=headers)
htm = htm.text.encode('latin-1').decode('unicode_escape')
print htm