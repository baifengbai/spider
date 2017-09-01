# -*- coding: utf-8 -*
import urllib2
import sys
from bs4 import BeautifulSoup
import time

reload(sys)
sys.setdefaultencoding("utf-8")


def get_1(i):
    url = "http://www.gaokaoq.com/score/index.html?type=1&city=13&collegeCity=0&batch=0&year=2011&q=&p=" + str(i)
    headers = {"Cookie": "td_cookie=18446744071243533036; "
                         "PHPSESSID=iohrkqft93jdjn8e95re34ogv4; "
                         "__jsluid=0282995e257f52d0b0d98899e29cf46a; "
                         "UM_distinctid=15dac1f830998-0ecd80e86b5e4d-4"
                         "74b0421-100200-15dac1f830a3e2; td_cookie=1844"
                         "6744071182462786; w_phone=b7dehfw8Leq8RKBCM4"
                         "yNHFVU7gUp2zpfVRyi77llbAf%2FBi6ENlnh1Q; "
                         "w_password=fc1diu6M5om1ZwpJiFKQhYmEBgszyl"
                         "F5A59s04%2BIG0GLmsM; w_tobe=3c3e8y2qoM8hIP"
                         "pgTpshlRdSS2nF0d%2F0hb8OBcY; w_gold_tip=200; "
                         "w_gold_tip_title=%E6%B3%A8%E5%86%8C; CNZZDAT"
                         "A1255363830=1422050311-1501828863-%7C1503535"
                         "630; Hm_lvt_fd9bf00761167d2e9689ba3d37779881"
                         "1501831333; Hm_lpvt_fd9bf00761167d2e9689ba3d"
                         "37779881=1503539248"}
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    hd = response.read()
    # print hd
    soup = BeautifulSoup(hd, 'lxml')
    body = soup.select(" div.school_lines ")
    print body.__len__()
    if body.__len__() == 1:
        soup_td = BeautifulSoup(str(body[0]), 'lxml')
        lines = soup_td.select(" td ")
        j = 9
        file_2 = file("fenshu_quan_1", 'a+')
        while j < lines.__len__():
            print lines[j].get_text(), lines[j+1].get_text(), \
                lines[j+2].get_text(), lines[j+3].get_text(), \
                lines[j+4].get_text(), lines[j+5].get_text(), \
                lines[j+6].get_text(), lines[j+7].get_text(), \
                lines[j+8].get_text()
            new_n = (lines[j].get_text() + "*" + lines[j+1].get_text() + "*" +
                     lines[j+2].get_text() + "*" + lines[j+3].get_text() + "*"
                     + lines[j+4].get_text() + "*" + lines[j+5].get_text() +
                     "*" + lines[j+6].get_text() + "*" + lines[j+7].get_text()
                     + "*" + lines[j+8].get_text() + "\n")
            file_2.write(new_n)
            j += 9
        file_2.close()


def main():
    i = 1
    while i < 84:
        get_1(i)
        time.sleep(1)
        i += 1


if __name__ == "__main__":
    main()
