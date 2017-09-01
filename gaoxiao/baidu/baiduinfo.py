# -*- coding: utf-8 -*
# 作废
import time
import urllib
import urllib2
import json
from bs4 import BeautifulSoup
import sys

reload(sys)
sys.setdefaultencoding('utf8')


def getinfo():
    file1 = open('E:\\school\\schoollist\\baiduschool')
    for lines in file1:
        time.sleep(0.3)
        print lines
        url = lines.split("*")[1].replace("\n", '')
        data = {}
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36",
            'Referer': "https://baike.baidu.com/wikitag/taglist?tagId=60829"}
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        # print response.read()
        hd = response.read()
        # print hd
        soup = BeautifulSoup(hd, 'lxml')
        lines = soup.select(" div.basic-info > dl > dt ")
        print lines.__len__()
        lines1 = soup.select(" div.basic-info > dl > dd ")
        print lines1.__len__()
        if lines.__len__() == lines1.__len__():
            i = 0
            while i < lines.__len__():
                if '中文名' in lines[i].get_text():
                    print "中文名" + lines1[i].get_text()
                elif '英文名' in lines[i].get_text():
                    print "英文名" + lines1[i].get_text()
                elif '简称' in lines[i].get_text().replace(" ", ''):
                    print "简称" + lines1[i].get_text().replace(" ", '')
                elif '创办时间' in lines[i].get_text():
                    print "创办时间" + lines1[i].get_text()
                elif '学校类型' in lines[i].get_text():
                    print "学校类型" + lines1[i].get_text()
                elif '属性' in lines[i].get_text().replace(" ", ''):
                    print "属性" + lines1[i].get_text().replace(" ", '')
                elif '所属地区' in lines[i].get_text():
                    print "所属地区" + lines1[i].get_text()
                elif '现任校长' in lines[i].get_text():
                    print "现任校长" + lines1[i].get_text()
                elif '知名校友' in lines[i].get_text():
                    print "知名校友" + lines1[i].get_text()
                elif '主管部门' in lines[i].get_text():
                    print "主管部门" + lines1[i].get_text()
                elif '硕士点' in lines[i].get_text():
                    print "硕士点" + lines1[i].get_text()
                elif '博士点' in lines[i].get_text():
                    print "博士点" + lines1[i].get_text()
                elif '博士后流动站' in lines[i].get_text():
                    print "博士后流动站" + lines1[i].get_text()
                elif '校    训' in lines[i].get_text():
                    print "校训" + lines1[i].get_text()
                elif '校    歌' in lines[i].get_text():
                    print "校    歌" + lines1[i].get_text()
                elif '专职院士' in lines[i].get_text():
                    print "专职院士" + lines1[i].get_text()
                elif '主要院系' in lines[i].get_text():
                    print "主要院系" + lines1[i].get_text()
                elif '国家重点学科' in lines[i].get_text():
                    print "国家重点学科" + lines1[i].get_text()
                elif '学校地址' in lines[i].get_text():
                    print "学校地址" + lines1[i].get_text()
                elif '学校代码' in lines[i].get_text():
                    print "学校代码" + lines1[i].get_text()
                elif '主要奖项' in lines[i].get_text():
                    print "主要奖项" + lines1[i].get_text()
                elif '校庆日' in lines[i].get_text():
                    print "校庆日" + lines1[i].get_text()
                elif '校    风' in lines[i].get_text():
                    print "校    风" + lines1[i].get_text()
                elif '两院院士' in lines[i].get_text():
                    print "两院院士" + lines1[i].get_text()
                elif '长江学者' in lines[i].get_text():
                    print "长江学者" + lines1[i].get_text()
                elif '文科资深教授' in lines[i].get_text():
                    print "文科资深教授" + lines1[i].get_text()
                elif '学术传统' in lines[i].get_text():
                    print "学术传统" + lines1[i].get_text()
                elif '发展定位' in lines[i].get_text():
                    print "发展定位" + lines1[i].get_text()
                elif '党委书记' in lines[i].get_text():
                    print "党委书记" + lines1[i].get_text()

                i += 1
                # time.sleep(10)


if __name__ == '__main__':
    getinfo()
