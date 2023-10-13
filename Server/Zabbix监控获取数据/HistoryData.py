#coding=utf-8
#获取监控项的数据
import json
import urllib2
# 基本请求参数
url = ""
header = {"Content-Type":"application/json"}
# request json
data = json.dumps(
{
   "jsonrpc":"2.0",
   "method":"history.get",
   "params":{
       "output":"extend",
       "history":3,
       "itemids":"284223",
       "limit":10
   },
   "auth":"",
   "id":1,
})
# 发送与读取数据
request = urllib2.Request(url,data)
for key in header:
   request.add_header(key,header[key])
try:
   result = urllib2.urlopen(request)
except urllib2.HTTPError as e:
   if hasattr(e, 'reason'):
       print 'We failed to reach a server.'
       print 'Reason: ', e.reason
   elif hasattr(e, 'code'):
       print 'The server could not fulfill the request.'
       print 'Error code: ', e.code
else:
   response = json.loads(result.read())
   result.close()
   print "Number Of Hosts: ", len(response['result'])
   for host in response['result']:
       print host