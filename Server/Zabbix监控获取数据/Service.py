#coding=utf-8
#获取服务器的登录令牌
import json
import urllib2
# 基本请求参数
url = ""
header = {"Content-Type":"application/json"}
# 用户名与密码
data = json.dumps(
{
   "jsonrpc": "2.0",
   "method": "user.login",
   "params": {
   "user": "your usernamer",
   "password": "your password"
},
"id": 0
})
# 发送请求
request = urllib2.Request(url,data)
for key in header:
   request.add_header(key,header[key])
try:
   result = urllib2.urlopen(request)
except urllib2.HTTPError as e:
   print "请求失败",e.code
else:
   response = json.loads(result.read())
   result.close()
print"请求成功，登录令牌为:",response['result']