自己工作生活中些的一些常用的Python脚本工具，已经去除了敏感的数据部分。
 
>    部分脚本可能使用了Python2，一版但是大部分使用的都是Python3.6以上版本,一版Python2脚本写的print都没加括号，还有coding指定
#### 说明
1. Web Spider文件夹
    写的一些爬虫脚本：
   - [spiderDYTT](./Web%20Spider/spiderDYTT.py)：电影天堂最新电影爬虫
   - [spiderMP4](./Web%20Spider/spiderMP4ba.py)：mp4吧电影数据爬虫
   - [720comDownload](./Web%20Spider/720comVRImgDownloader.py):720全景网图片下载，好像已经无法使用了
   - 

2. File Handler文件夹 文件处理脚本：
   - [log2Excel](./File%20Handler/log2Excel.py)：本文文件转excel,其实就是一个读取文本文件转成Excel的脚本
   - [edge-tts](./File%20Handler/degeTts):文本转语音脚本，调用edge-tts服务

3. Time文件夹 时间相关的处理脚本:
    - [timestamp2LocalTime](./Time/timestamp2LocalTime.py): 一个简单的输入毫秒时间戳转成时间的命令行脚本

4. Server文件夹 服务器相关的监控脚本：
    - [zabbix监控API获取数据](./Server/Zabbix监控获取数据):新增Zabbix监控API获取数据的Python代码，从登录获取token到获取到数据
    - [processWatcher](./Server/prccessWatch.py)：Linux中的简单进程监控脚本，输出Log，现在这个脚本的是Nginx监控
    - [webUrlWatcher](./Server/webUrlWatcher.py):Web URL的打开请求监控，定时检测网址是不是能打开，输出Log

5. PythonCV文件夹 一些练手的图片视觉算法:
    - [FaceRecognition](./PythonCV/FaceRecognition) 为OpenCV简单的人脸识别的例子，使用到的是官方的人脸库
    - [pytesser](./PythonCV/Pytesser) 图片识别与转换文字
    - [FindContour](./PythonCV/FindContour) 为在一张图片上寻找一个矩形的框图，并裁剪出来
    - [bHash](./PythonCV/bHash) bHash图片指纹算法，确定两张图片的相似程度 
   
6. DB文件夹 一些为数据库写的脚本：
   - [db](./DB/db.py) 基础本地连接脚本，提供了常见的一些CURD方法
   
7. SimpleProject 一些成品的简单工程：
   - [年会抽奖](./SimpleProject/lucky年会抽奖)：Flask做的一个简单的抽奖项目，年会抽奖，按空格键可以停止，数据记录到数据库,还有一个简单的音乐控台HTML播放音乐





