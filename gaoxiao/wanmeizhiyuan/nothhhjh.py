import sys, httplib, urllib, random
params = "value=xxx"
ipAddress = "10.0.0.1"
headers = { "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Encoding":"gzip, deflate", "Accept-Language":"zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3", "Connection":"keep-alive", "X-Forwarded-For":ipAddress, "Content-Length":"31", "Content-Type":"application/x-www-form-urlencoded", "User-Agent":"Mozilla/5.0 (Windows NT 5.1; rv:11.0) Gecko/20100101 Firefox/11.0" }
con2 = httplib.HTTPConnection("10.0.0.2")
try:
    con2.request("POST", "/xxx.php", params, headers)
except Exception, e:
    print e
    sys.exit(1)
r2 = con2.getresponse()
print r2.read()