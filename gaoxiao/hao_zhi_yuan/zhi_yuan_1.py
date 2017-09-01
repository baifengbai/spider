# -*- coding: utf-8 -*
import sys
import urllib2
import time
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding("utf-8")


def get_fen(i):
    url = "http://www.zggkbk.com/index.php?s=/Index/college_score_" \
          "line/pi/0/l/0/sd/0/y/0/lb/0/p/" + str(i) + ".html"
    headers = {"cookie": "PHPSESSID=jri2bik2e4v33p4imhd0u35jf3; "
                        "user_name=18656087017; "
                        "user_pass=b9e1763eb9eb4f0b773239bcf534165c; "
                        "yunsuo_session_verify=f1c4c7a95716192309"
                        "0d99c892192b9d; think_template=default; thi"
                        "nk_language=0; Hm_lvt_8395e481bfa7cc58f345c8f"
                        "3977d1b96=1503451198; Hm_lpvt_8395e481bfa7cc"
                        "58f345c8f3977d1b96=1503451793; Hm_lvt_95bd6"
                        "93eebdd22afc5d0329e6e9ec961=1500902000,1500"
                        "902114,1503451198; Hm_lpvt_95bd693eebdd22af"
                        "c5d0329e6e9ec961=1503451794"}
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    hd = response.read()
    # print hd
    soup = BeautifulSoup(hd, 'lxml')
    grade = soup.select(" div.grade ")
    print grade.__len__()
    soup_td = BeautifulSoup(str(grade[0]), 'lxml')
    lines = soup_td.select(" td ")
    # print lines.__len__()
    j = 0
    file_2 = file("hao_fen", 'a+')
    while j < lines.__len__():
        new_n = (lines[j].get_text() + "*" + lines[j + 1].get_text() + "*" +
                 lines[j + 2].get_text() + "*" + lines[j + 3].get_text() + "*" +
                 lines[j + 4].get_text() + "*" + lines[j + 5].get_text() + "*" +
                 lines[j + 6].get_text() + "*" + lines[j + 7].get_text() + "*" +
                 lines[j + 8].get_text() + "\n")
        file_2.write(new_n)
        j += 9
    file_2.close()
    time.sleep(1)


def main():
    i = 1
    while i < 1473:
        get_fen(i)
        i += 1


if __name__ == "__main__":
    main()
