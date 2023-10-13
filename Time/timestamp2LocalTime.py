#coding:utf-8
import time
while(1):
    # 获得时间戳
    now =int(raw_input("input your unix time: "))
    # 转换为其他日期格式
    timeArray = time.localtime(now)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    print("your time is "+ otherStyleTime)