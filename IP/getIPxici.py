import telnetlib
import urllib2
from bs4 import BeautifulSoup
from multiprocessing import Pool
import multiprocessing

def testIP(lines,llst):
    # IPok=[]
    try:
        telnetlib.Telnet(str(lines).split("\t")[0], port=str(lines).split("\t")[1], timeout=2)
    except:
        print 'connect failed'
        pass
    else:
        print 'success'
        llst.append(str(lines).split("\t")[0]+":"+str(lines).split("\t")[1])


def getIPs(i):
    list=[]
    url='http://www.xicidaili.com/nn/'+str(i)
    headers={}
    headers['User-Agent']='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'
    headers['Cookie']='td_cookie=18446744069516755738; _free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJTkwZDc2YjY0YzNhZjc3ZGUyMTQ0MzcwMjYyNjk5YTkxBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMUtSSndwanZ1bUVDVnRFdHVNTFdSWElxdzJoRjM1ZkswbUlDbjZKMm03RTA9BjsARg%3D%3D--5c90fbc75d871f65e43b09f47defa73c854fe14d; td_cookie=18446744073571851019; Hm_lvt_0cf76c77469e965d2957f0553e6ecf59=1500463976; Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59=1501814259'
    try:
        request = urllib2.Request(url,headers=headers)
        response = urllib2.urlopen(request)
    except:
        request = urllib2.Request(url,headers=headers)
        response = urllib2.urlopen(request)
    hd=response.read()
    soup=BeautifulSoup(hd,'lxml')
    lines=soup.select(" tr > td ")
    print lines.__len__()
    j=0
    while j<lines.__len__():
        list.append(str(lines[j+1].get_text()).replace(" ",'')+"\t"+str(lines[j+2].get_text()).replace(" ",''))
        j+=10

    mgr = multiprocessing.Manager()
    llst=mgr.list()
    pool = Pool(processes=6)
    for liness in list:
        pool.apply_async(testIP, args=(liness,llst))
    pool.close()
    pool.join()
    #return IPok


    return llst


def getxici():
    i=1
    tq=[]
    while i <3:
        list = []
        list = getIPs(i)
        # print list.__len__()
        tq.extend(list)
        i += 1
    return tq


if __name__=='__main__':
    i=1
    tq=[]
    while i <3:
        list=[]
        list=getIPs(i)
        print list.__len__()
        i+=1
