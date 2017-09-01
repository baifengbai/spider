import telnetlib
import urllib2
from bs4 import BeautifulSoup
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


def getIPs():
    list = []
    url = 'http://www.89ip.cn/apijk/?&tqsl=200&sxa=&sxb=&tta=&ports=&ktip=&cf=1'
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'
    # headers['Cookie']='__jsluid=b96693d21e33e599750c8b14263094d5; UM_distinctid=15d5aee2a032df-079a7a03674693-474b0421-100200-15d5aee2a04762; CNZZDATA1253901093=720767245-1500466963-null%7C1501811796; Hm_lvt_1761fabf3c988e7f04bec51acd4073f4=1500469144,1501815838; Hm_lpvt_1761fabf3c988e7f04bec51acd4073f4=1501815927; td_cookie=18446744069520568683'
    try:
        request = urllib2.Request(url,headers=headers)
        response = urllib2.urlopen(request)
    except:
        request = urllib2.Request(url,headers=headers)
        response = urllib2.urlopen(request)
    hd=response.read()
    #soup=BeautifulSoup(hd,'lxml')
    #lines=soup.select(" tr > td ")
    lines=str(hd).split("<BR>")
    print lines.__len__()
    j=1
    while j<lines.__len__()-1:
        #print repr(lines)
        list.append(str(lines[j]).replace(" ",'').replace("\r\n\t\t",''))
        j+=1
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