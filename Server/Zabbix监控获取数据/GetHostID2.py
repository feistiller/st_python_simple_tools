#coding=utf-8
#获取服务器监控的组的服务器
import json
import urllib2
# 基本请求参数
url = ""
header = {"Content-Type":"application/json"}
# request json
data = json.dumps(
{
   "jsonrpc":"2.0",
   "method":"host.get",
   "params":{
       "output":["hostid","name"],
       "groupids":"39",
   },
   "auth":"",
   "id":1,
})
# create request object
request = urllib2.Request(url,data)
for key in header:
   request.add_header(key,header[key])
# get host list
try:
   result = urllib2.urlopen(request)
except URLError as e:
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
       print "Host ID:",host['hostid'],"HostName:",host['name']
