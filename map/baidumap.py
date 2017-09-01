# -*- coding: utf-8 -*
import ghost
from ghost import Ghost

g = Ghost()
url="http://api.map.baidu.com/lbsapi/getpoint/index.html"
with g.start() as session:

   page, extra_resources = session.open(url)
   print page.url
   #print page.headers
   print session.exists('#localsearch')
   print session.exists('#localvalue')
   print session.set_field_value("#localvalue","合肥市蜀麓小学")
   #print session.set_field_value("#mctY", "655756756")
   #session.evaluate_js_file("text/javascript/mecGeo")
   #print session.click('#localsearch',btn=0,)
   print session.fire('#localsearch','click')
   print session.evaluate("localsearch()")
   print session.evaluate("loadBody()")
   print session.evaluate("function()")
   print session.exists("#txtPanel")

   #print session.content
   print page.content
   if page.http_status == 200 :
       print("OK!")
#g1.open(url)
#result, resources = g1.evaluate("document.getElementById('mctGeo').click();", expect_loading=True)
#print result