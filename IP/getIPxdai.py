import telnetlib
import urllib2
from bs4 import BeautifulSoup
from multiprocessing import Pool
import multiprocessing
import json
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


def getIPs():
    list=[]
    url='http://www.xdaili.cn/ipagent//freeip/getFreeIps?page=1&rows=10'
    headers={}
    headers['User-Agent']='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'
    headers['Cookie'] = 'aliyungf_tc=AQAAAMNNdyNWzwoAWVcHJB+CvSkznc5k; UM_distinctid=15dcb68881f552-0947d13a6603e7-474b0421-100200-15dcb68882066d; CNZZDATA1260873131=1791161928-1502355533-%7C1502433529; _ga=GA1.2.1389335055.1502356213; _gid=GA1.2.1178865580.1502356213; Hm_lvt_c1c9e8373d7f000ad58265f0b17f1cff=1502356212; Hm_lpvt_c1c9e8373d7f000ad58265f0b17f1cff=1502437050; td_cookie=18446744070141437475'
    try:
        request = urllib2.Request(url,headers=headers)
        response = urllib2.urlopen(request)
    except:
        request = urllib2.Request(url,headers=headers)
        response = urllib2.urlopen(request)
    hd=response.read()
    #print hd
    json_h=json.loads(hd)
    for lines in json_h["RESULT"]["rows"]:
        list.append(str(lines["ip"])+":"+str(lines["port"]))
    #print list
    mgr = multiprocessing.Manager()
    llst=mgr.list()
    pool = Pool(processes=6)
    for liness in list:
        pool.apply_async(tePro, args=(liness,llst))
    pool.close()
    pool.join()
    #return IPok
    return llst
    #return list

if __name__=='__main__':
    i=1
    tq=[]
    while i <2:
        list=[]
        list=getIPs()
        print list.__len__()
        print list
        i+=1