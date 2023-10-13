#coding=utf-8
#获得监控的组
import json
import urllib2
# 基本请求参数
url = ""
header = {"Content-Type":"application/json"}
# request json
data = json.dumps(
{
   "jsonrpc":"2.0",
   "method":"hostgroup.get",
   "params":{
       "output":["groupid","name"],
   },
   "auth":"", # Service中获得的登录令牌
   "id":1,
})
# 发送请求
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
   print "Hosts总数: ", len(response['result'])
   #打印
   for group in response['result']:
       # 格式化显示
       print "组 ID:",group['groupid'],"\tGroupName:",group['name']