# -*- coding: utf-8 -*
import ghost
from ghost import Ghost
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
g = Ghost()
url="http://www.site-digger.com/tools/mct2latlng.html"
#page, extra_resources = g.open("http://www.site-digger.com/tools/mct2latlng.html")
with g.start() as session:

   page, extra_resources = session.open("http://www.site-digger.com/tools/mct2latlng.html")
   #print page.content
   print page.url
   print page.headers
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
#g1.open(url)
#result, resources = g1.evaluate("document.getElementById('mctGeo').click();", expect_loading=True)
#print result