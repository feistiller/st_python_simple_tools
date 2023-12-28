import webbrowser
import time
import os

url = "http://www.example.com"

# 创建一个新的浏览器实例（这里请求的是edge）
edge = webbrowser.get('C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s')

# 使用 Edge 浏览器打开网页
edge.open(url)
# 等待一段时间
time.sleep(10)

# 关闭 Edge 浏览器
os.system("taskkill /im msedge.exe /f")