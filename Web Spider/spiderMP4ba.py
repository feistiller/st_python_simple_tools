# coding:utf-8
# MP4吧爬虫

from bs4 import BeautifulSoup
import urllib2
import time
import re
import sys

base = 'http://www.mp4ba.net/forum-mp4ba-'


# 获得该页
def getMovieUrl(url):
    web = urllib2.urlopen(url)
    soup = BeautifulSoup(web, "lxml")
    print "读取网页中，请等待"
    time.sleep(1)
    return soup.find_all('a', class_="s xst")


# 获得下载地址
def getDownloadUrl(url):
    web = urllib2.urlopen(url)
    soup = BeautifulSoup(web, "lxml")
    print "读取网页中，请稍后"
    time.sleep(1)
    return soup.find_all('a', href=re.compile("magnet:*"))


# main function
def main():
    f = open('./Data/Mp4.data', 'a')
    f.write("开始运行\n")
    # 循环1000页
    # 计数器
    j = 1
    for i in range(1, 1000):
        print "打开第" + str(i) + "页"
        time.sleep(0.5)
        url = base + str(i) + ".html"
        movieUrls = getMovieUrl(url)
        for movieUrl in movieUrls:
            print movieUrl
            temp_url = movieUrl['href']
            print "准备打开" + temp_url
            print "写入第" + str(j) + "行"
            j += 1
            f.write(movieUrl.string + '\n')
            time.sleep(0.5)
            temp_download_url = getDownloadUrl(temp_url)
            print "写入第" + str(j) + "行"
            if temp_download_url:
                f.write(temp_download_url[0]['href'] + '\n')
            else:
                f.write("暂无" + '\n')
            j += 1
            time.sleep(0.5)
    f.close()
    # return


# 入口
if __name__ == '__main__':
    reload(sys)
    # change coding
    sys.setdefaultencoding('utf-8')
    main()
