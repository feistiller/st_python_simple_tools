# coding:utf-8
# 电影天堂爬虫
from bs4 import BeautifulSoup
import urllib2
import time
import re
import sys
import xlwt


# getUrl
def getMovieUrl(url):
    response = urllib2.urlopen(url)
    if (response == ''):
        print "read url failed"
        exit()
    else:
        print "read url success"
    soup = BeautifulSoup(response, "lxml")
    # sleep 2 sec and continue
    print "waiting 1 sec"
    time.sleep(1)
    print soup.find_all('a')[1]['href']
    print "get newMovie url"
    return soup.find_all('a')[1]['href']


# getMovieList
def getMovieList(url):
    try:
        response = urllib2.urlopen(url)
    except:
        print '结束运行'
        exit()

    if (response == ''):
        print "read ListUrl failed"
        exit()
    else:
        print "read ListUrl success"
    soup = BeautifulSoup(response, "lxml")
    print "waiting 1 sec"
    time.sleep(1)
    return soup.find_all("a", class_="ulink")


# getDownloadURL
def getDownLoadList(url):
    try:
        response = urllib2.urlopen(url)
    except:
        response = urllib2.urlopen(url)
    if (response == ''):
        print "read DownloadUrl failed"
        exit()
    else:
        print "read DownloadUrl success"
    soup = BeautifulSoup(response, "lxml")
    print "waiting 1 sec"
    time.sleep(1)
    print url
    return soup.find('a', text=re.compile("ftp://*"))


# get every page url
def getPageUrl(url):
    response = urllib2.urlopen(url)
    if (response == ''):
        print "read DownloadUrl failed"
        exit()
    else:
        print "read DownloadUrl success"
    soup = BeautifulSoup(response, "lxml")
    print "waiting 1 sec"
    time.sleep(1)
    return soup.find('option', text=1)


# 入口
def main():
    # workbook = xlwt.Workbook(encoding='utf-8')
    # sheet = workbook.add_sheet('test', cell_overwrite_ok=True)
    baseUrl = 'http://www.ygdy8.net/'
    f = open('DYTT.log', 'a')
    f.write("开始运行\n")

    # 此时的页码是第一页（此页面默认地址并非是需要的页面地址）
    # 获取所有的页码地址
    lastNewUrl = getMovieUrl(baseUrl + 'index.html')
    pageUrl = getPageUrl(baseUrl + lastNewUrl)
    # 会拿到第一页的url
    # 重构url
    # base_pageUrl=(lastNewUrl)
    reObj1 = re.compile('(\w\S+/\S+/)')
    temp_page_url = reObj1.findall(lastNewUrl)

    reObj2 = re.compile('(\S+_)')
    temp_page_url_cox = reObj2.findall(pageUrl['value'])
    # print temp_page_url_cox

    j = 1
    for i in range(1, 300):
        full_url = baseUrl + temp_page_url[0] + temp_page_url_cox[0] + str(i) + '.html'
        print '正在读取' + str(i) + '页'
        print '地址为' + full_url
        time.sleep(5)
        movieUrlList = getMovieList(full_url)
        # f.write("***************************获得地址:" + full_url + '\n')
        for url in movieUrlList:
            print "reading url"
            # print url
            timeNow = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            f.write(str(timeNow) + "获得mov地址：" + str(url) + '\n')
            print "正在写" + str(j) + "……"
            # sheet.write(j, 1, str(url.string))
            time.sleep(5)
            temp_url = getDownLoadList(baseUrl + url['href'] + '\n')
            # sheet.write(j, 2, str(temp_url['href']))
            j += 1
            # print temp_url['href']
            f.write(str(timeNow) + "获得mov下载：" + str(temp_url['href'] + '\n'))
    f.close()
    # workbook.save('example.xls')


# 入口
if __name__ == '__main__':
    reload(sys)
    # change coding
    sys.setdefaultencoding('utf-8')
    main()
