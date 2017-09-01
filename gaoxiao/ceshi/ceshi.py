# -*- coding: utf-8 -*
#  作废
import ghost
from ghost import Ghost
import sys
import time
reload(sys)
sys.setdefaultencoding("utf-8")
g = Ghost()
url="http://www.site-digger.com/tools/mct2latlng.html"
#page, extra_resources = g.open("http://www.site-digger.com/tools/mct2latlng.html")
with g.start() as session:

   page, extra_resources = session.open("http://www.apesk.com/mbti/dati.asp")
   #print page.content
   print page.url
   print page.headers
   print session.click('.green.button', btn=0)
   print session.click('.green.button', btn=0)
   print session.exists(".11")
   print session.exists("#tip7")
   print session.exists("#datitable")
   print session.exists("#biankuang")
   print session.exists("#kaishi")
   print session.exists("[name='answer1']")
   print session.set_field_value("[name='answer1']","1")
   time.sleep(1)
   print session.set_field_value("[name='answer2']", "1")
   print session.set_field_value("[name='answer3']", "1")
   time.sleep(1)
   print session.set_field_value("[name='answer4']", "1")
   print session.set_field_value("[name='answer5']", "1")
   time.sleep(1)
   print session.set_field_value("[name='answer6']", "1")
   print session.set_field_value("[name='answer7']", "1")
   time.sleep(1)
   print session.set_field_value("[name='answer8']", "1")
   print session.set_field_value("[name='answer9']", "1")
   time.sleep(1)
   print session.set_field_value("[name='answer10']", "1")
   time.sleep(1)
   print session.set_field_value("[name='answer11']", "1")
   print session.set_field_value("[name='answer12']", "1")
   print session.set_field_value("[name='answer13']", "1")
   time.sleep(1)
   print session.set_field_value("[name='answer14']", "1")
   print session.set_field_value("[name='answer15']", "1")
   time.sleep(1)
   print session.set_field_value("[name='answer16']", "1")
   time.sleep(1)
   print session.set_field_value("[name='answer17']", "1")
   print session.set_field_value("[name='answer18']", "1")
   time.sleep(1)
   print session.set_field_value("[name='answer19']", "1")
   print session.set_field_value("[name='answer20']", "1")
   print session.set_field_value("[name='answer21']", "1")
   time.sleep(1)
   print session.set_field_value("[name='answer22']", "1")
   print session.set_field_value("[name='answer23']", "1")
   time.sleep(1)
   print session.set_field_value("[name='answer24']", "1")
   time.sleep(1)
   print session.set_field_value("[name='answer25']", "1")
   print session.set_field_value("[name='answer26']", "1")
   time.sleep(1)
   print session.set_field_value("[name='answer27']", "1")
   time.sleep(1)
   print session.set_field_value("[name='answer28']", "1")
   print session.set_field_value("[name='sex']", "male")
   print session.set_field_value("[name='nianling']", "00")
   print session.click('.green.button', btn=0)
   print session.content
'''
   print session.exists('input:enabled')
   print session.exists('#mctX')
   print session.set_field_value("#mctX","12128773")
   print session.set_field_value("#mctY", "6557567")
   #session.evaluate_js_file("text/javascript/mecGeo")
   #print session.click('input:enabled',btn=0)
   #print session.fire('input:enabled','click')
   print session.evaluate("mctGeo()")

   #session.show()
   #print session.content
   lng=session.content.split('经纬度lng:')[1].split("<")[0].strip()
   lat = session.content.split('经纬度lat:')[1].split("<")[0].strip()
   print lng
   print lat

   #print page._reply
   #print page.session.logger.info

   if page.http_status == 200 :
       print("OK!")
'''
#g1.open(url)
#result, resources = g1.evaluate("document.getElementById('mctGeo').click();", expect_loading=True)
#print result