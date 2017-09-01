# -*- coding: utf-8 -*
# 作废
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
   print session.click("[for='11']", btn=0)
   print session.click("[for='21']", btn=0)
   print session.click("[for='31']", btn=0)
   print session.click("[for='41']", btn=0)
   print session.click("[for='51']", btn=0)
   print session.click("[for='61']", btn=0)
   print session.click("[for='71']", btn=0)
   print session.click("[for='81']", btn=0)
   print session.click("[for='91']", btn=0)
   print session.click("[for='101']", btn=0)
   print session.click("[for='111']", btn=0)
   print session.click("[for='121']", btn=0)
   print session.click("[for='131']", btn=0)
   print session.click("[for='141']", btn=0)
   print session.click("[for='151']", btn=0)
   print session.click("[for='161']", btn=0)
   print session.click("[for='171']", btn=0)
   print session.click("[for='181']", btn=0)
   print session.click("[for='191']", btn=0)
   print session.click("[for='201']", btn=0)
   print session.click("[for='211']", btn=0)
   print session.click("[for='221']", btn=0)
   print session.click("[for='231']", btn=0)
   print session.click("[for='241']", btn=0)
   print session.click("[for='251']", btn=0)
   print session.click("[for='261']", btn=0)
   print session.click("[for='271']", btn=0)
   print session.click("[for='281']", btn=0)
   print session.click("[for='291']", btn=0)
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