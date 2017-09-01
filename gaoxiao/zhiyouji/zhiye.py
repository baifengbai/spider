# -*- coding: utf-8 -*
"""职业的一些信息"""
import sys
import urllib2
import time
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding("utf-8")


# 去重
def to_one():
    file_2 = file("list_m")
    list_m = []
    for lines in file_2:
        print lines.replace("\n", '')
        list_m.append(lines.replace("\n", ''))
    print list_m.__len__()
    print list(set(list_m)).__len__()
    file_y = file('list_z.txt', 'a+')
    for line_34 in list(set(list_m)):
        file_y.write(line_34)
        file_y.write("\n")
    file_y.close()
    file_2.close()


def g_gang(name, href):
    url = "http://www.jobui.com" + href
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    hd = response.read()
    # print hd
    soup = BeautifulSoup(hd, 'lxml')


def jiu_ye(name):
    url = "http://www.jobui.com/trends/全国-" + name + "/"
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    hd = response.read()
    # print hd
    soup = BeautifulSoup(hd, 'lxml')
    bar_list = soup.findAll(class_='barlist-list cfix')
    if bar_list.__len__() == 2:
        soup_num = BeautifulSoup(str(bar_list[0]), 'lxml')
        title_1 = soup_num.select(" span.barlist-title ")
        num_1 = soup_num.select(" em.ffgg ")
        print title_1.__len__(), num_1.__len__()
        if title_1.__len__() == num_1.__len__() and num_1.__len__() == 10:
            file_1 = file("E:\\school\\zhiye\\z\\area_x", 'a+')
            for i_2 in range(0, 10):
                print title_1[i_2].get_text(), num_1[i_2].get_text()
                file_1.write(str(name))
                file_1.write("*")
                file_1.write(str(title_1[i_2].get_text()).replace("\n", ""))
                file_1.write("*")
                file_1.write(str(num_1[i_2].get_text()).replace("\n", ''))
                file_1.write("\n")
            file_1.close()

        soup_salary = BeautifulSoup(str(bar_list[1]), 'lxml')
        title_2 = soup_salary.select(" span.barlist-title ")
        num_2 = soup_salary.select(" span.barlist-value > em.ffgg ")
        print title_2.__len__(), num_2.__len__()
        if title_2.__len__() == num_2.__len__() and num_2.__len__() == 10:
            file_2 = file("E:\\school\\zhiye\\z\\area_s", 'a+')
            for i_3 in range(0, 10):
                print title_2[i_3].get_text(), num_2[i_3].get_text()
                file_2.write(str(name))
                file_2.write("*")
                file_2.write(str(title_2[i_2].get_text()).replace("\n", ""))
                file_2.write("*")
                file_2.write(str(num_2[i_2].get_text()).replace("\n", ''))
                file_2.write("\n")
            file_2.close()


def main(zhi_):
    print zhi_
    url = "http://www.jobui.com/salary/?" \
          "cityKw=%E5%85%A8%E5%9B%BD&jobKw=" + zhi_
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    hd = response.read()
    # print hd
    soup = BeautifulSoup(hd, 'lxml')
    is_found = soup.findAll(class_="tac fs18 gray9")
    if is_found.__len__() == 1:
        if "找不到和" in is_found[0].get_text():
            print "找不到"
        else:
            print "------------------------wenti---------------------"
    else:
        qu_jian = soup.findAll(class_="statistics-numbox j-numbox")
        # qujian
        if qu_jian.__len__() == 1:
            soup_2 = BeautifulSoup(str(qu_jian[0]), 'lxml')
            section_val = soup_2.select(" span.section-val ")
            specific_val = soup_2.select("span.specific-val")
            if section_val.__len__() == specific_val.__len__():
                file_salary = file("E:\\school\\zhiye\\z\\salary", 'a+')
                for i_2 in range(1, section_val.__len__()):
                    new_n_1 = (str(zhi_) + "*" + str(
                        section_val[i_2].get_text()) + "*" +
                               str(specific_val[i_2].get_text()) + '\n')
                    print new_n_1
                    file_salary.write(new_n_1)
                file_salary.close()
            else:
                print "区间 占比 don't match"

        file_salary_ave = file("E:\\school\\zhiye\\z\\salary_ave", 'a+')
        salary_avger = soup.findAll(class_='salary-avger')
        print salary_avger[0].get_text()[2:]
        num_salary = soup.findAll(class_='fs18 fwb box')
        print num_salary[0].get_text()[3:-11]
        file_salary_ave.write(str(zhi_) + "*" +
                              str(salary_avger[0].get_text()[2:]) + "*" +
                              str(num_salary[0].get_text()).replace("\n", '') +
                              "\n")
        file_salary_ave.close()

        work_len_data = soup.findAll(id='workLen-dataInfoss')
        print str(work_len_data[0].get_text()).replace("\n", '')
        file_work_len = file("E:\\school\\zhiye\\z\\work_len", 'a+')
        file_work_len.write(str(zhi_))
        file_work_len.write("*")
        file_work_len.write(str(work_len_data[0].get_text())
                            .replace("\r\n", '').replace("\n", '')
                            .replace("\t", '').replace(" ", ''))
        file_work_len.write("\n")
        file_work_len.close()

        hang = soup.findAll(class_="competitive fl jk-matter jk-box")
        if hang.__len__() == 1:
            soup_h = BeautifulSoup(str(hang[0]), 'lxml')
            line_1 = soup_h.select(" a.industry-sample ")
            line_2 = soup_h.select(" span.sample-number ")
            line_3 = soup_h.select(" em.money ")
            print line_1.__len__(), line_2.__len__(), line_3.__len__()
            if line_1.__len__() == line_2.__len__() \
                    and line_1.__len__() == line_3.__len__() \
                    and line_1.__len__() == 10:
                file_hang = file("E:\\school\\zhiye\\z\\hang", 'a+')
                for i_3 in range(0, 10):
                    print line_1[i_3].get_text()\
                        .replace(" ", "").replace("\n", '')
                    print line_2[i_3].get_text().replace("\r\n", '')
                    print line_3[i_3].get_text().replace("\n", '')
                    file_hang.write(str(zhi_))
                    file_hang.write("*")
                    file_hang.write(line_1[i_3].get_text().replace(
                        " ", "").replace("\r\n", '').replace(
                        "\t", "").replace("\n", ''))
                    file_hang.write("*")
                    temp_t = line_2[i_3].get_text()
                    if "个样本" in temp_t:
                        temp_t = str(temp_t).replace("个样本", '')
                    file_hang.write(
                        temp_t.replace("\r\n", '').replace(
                            "\t", '').replace('\n', ''))
                    file_hang.write("*")
                    file_hang.write(
                        line_3[i_3].get_text().replace("\n", '')[1:])
                    file_hang.write("\n")
                file_hang.close()

        area = soup.findAll(class_="competitive fr jk-matter jk-box")
        if area.__len__() == 1:
            soup_h = BeautifulSoup(str(area[0]), 'lxml')
            line_1 = soup_h.select(" a.areaCont ")
            line_2 = soup_h.select(" span.sample-number ")
            line_3 = soup_h.select(" em.money ")
            print line_1.__len__(), line_2.__len__(), line_3.__len__()
            if line_1.__len__() == line_2.__len__() \
                    and line_1.__len__() == line_3.__len__() \
                    and line_1.__len__() == 10:
                file_area = file("E:\\school\\zhiye\\z\\area", 'a+')
                for i_3 in range(0, 10):
                    print line_1[i_3].get_text()
                    print line_2[i_3].get_text()
                    print line_3[i_3].get_text()
                    file_area.write(str(zhi_))
                    file_area.write("*")
                    file_area.write(
                        line_1[i_3].get_text().replace(
                            " ", "").replace("\r\n", ''). replace(
                            "\t", "").replace("\n", ''))
                    file_area.write("*")
                    temp_t = line_2[i_3].get_text()
                    if "份样本" in temp_t:
                        temp_t = str(temp_t).replace("份样本", '')
                    file_area.write(
                        temp_t.replace("\r\n", '').replace(
                            "\t", '').replace('\n', ''))
                    file_area.write("*")
                    file_area.write(
                        line_3[i_3].get_text().replace("\n", '')[1:])
                    file_area.write("\n")
                file_area.close()
        jiu_ye(zhi_)
        gang = soup.select(" a.tab ")
        for g_g in gang:
            if "岗位职责" in g_g.get_text():
                g_gang(zhi_, g_g.get("href"))

    time.sleep(5)


if __name__ == "__main__":
    file_z = file("list_z.txt")
    for lines_z in file_z:
        main(lines_z.replace("\n", ''))
