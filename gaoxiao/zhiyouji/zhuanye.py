# -*- coding: utf-8 -*
"""hhhhhhhhhh--no question"""
# 职友集 专业对应的相关信息
import time
import urllib2
import sys
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding("utf-8")


def major(name, href):
    url = "http://edu.jobui.com" + href
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    hd = response.read()
    soup = BeautifulSoup(hd, 'lxml')
    body = soup.findAll(class_="modBar cfix jk-box jk-matter")
    if body.__len__() == 1:
        soup_bar = BeautifulSoup(str(body), 'lxml')
        bar_list = soup_bar.select(" div.barlist ")
        if bar_list.__len__() == 2:
            hang = bar_list[0]
            soup_hang = BeautifulSoup(str(hang), 'lxml')
            bar_name = soup_hang.select(" a.barlist-title-name ")
            bar_num = soup_hang.findAll(class_="fs12 gray9")
            bar_per = soup_hang.findAll(class_="fwb fr")
            print bar_name.__len__(), bar_num.__len__(), bar_per.__len__()
            if bar_name.__len__() == bar_num.__len__() and bar_num.__len__() ==\
                    bar_per.__len__() and bar_per.__len__() == 10:
                file_2 = file("E:\\school\\zhiye\\jiuye", "a+")
                for i_2 in range(0, 10):
                    print bar_name[i_2].get_text(), \
                        bar_num[i_2].get_text(), \
                        bar_per[i_2].get_text().replace("\n", '')
                    number = str(bar_num[i_2].get_text()).replace("\r\n", '').\
                        replace(" ", '').split("(")[1].split(")")[0]
                    if "份样本" in number:
                        number = number.replace("份样本", "")
                    new_n = (str(name) + "*" +
                             str(bar_name[i_2].get_text()) + "*" +
                             number + "*" +
                             str(bar_per[i_2].get_text().replace("\n", '')) +
                             "\n")
                    file_2.write(new_n)
                file_2.close()

            area = bar_list[1]
            soup_area = BeautifulSoup(str(area), 'lxml')
            area_name = soup_area.select(" a.barlist-title-name ")
            area_num = soup_area.findAll(class_="fs12 gray9")
            area_per = soup_area.findAll(class_="fwb fr")
            print area_name.__len__(), area_num.__len__(), area_per.__len__()
            if area_name.__len__() == area_num.__len__() and area_num.__len__()\
                    == area_per.__len__() and area_per.__len__() == 10:
                file_3 = file("E:\\school\\zhiye\\area", "a+")
                for i_3 in range(0, 10):
                    print area_name[i_3].get_text(), \
                        str(area_num[i_3].get_text()), \
                        area_per[i_3].get_text().replace("\n", '')
                    number = str(area_num[i_3].get_text()).replace(
                        "\r\n", '').replace(" ", '').split("(")[1].split(")")[0]
                    if "份样本" in number:
                        number = number.replace("份样本", "")
                    new_n = (str(name) + "*" +
                             str(area_name[i_3].get_text()) + "*" +
                             number + "*" +
                             str(area_per[i_3].get_text().replace("\n", '')) +
                             "\n")
                    file_3.write(new_n)
                file_3.close()
        else:
            print "no hangye or area"
    else:
        print "no body"


def main():
    url = "http://edu.jobui.com/majors/benke/"
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    # print response.read()
    hd = response.read()
    soup = BeautifulSoup(hd, 'lxml')
    body = soup.findAll(class_="jk-matter sbox")
    # print body[0]
    soup_lines = BeautifulSoup(str(body[0]), 'lxml')
    lines = soup_lines.select(" li.fl > a ")
    for line in lines:
        name = line.get_text()
        href = line.get("href")
        print name, href
        major(name, href)
        time.sleep(3)

if __name__ == "__main__":
    main()
