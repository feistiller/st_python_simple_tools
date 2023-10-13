import time
import urllib
import logging
import datetime

url = ""
now = datetime.datetime.now()
name = now.strftime('%Y-%m-%d')
log_filename = name + ".log"
i = 0
logging.basicConfig(filename='./log/'+log_filename, filemode='a+', level=logging.DEBUG)
while True:
    time.sleep(1)
    print 'web running' + str(i)
    i = int(i) + 1
    re_url = urllib.urlopen(url)
    if re_url:
        logging.info(now.strftime('%H:%M:%S')+"success")
    else:
        logging.warning(now.strftime('%H:%M:%S')+"fail")
