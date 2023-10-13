import os, sys, time,logging,datetime
while True:
    time.sleep(3)
    now = datetime.datetime.now()
    name = now.strftime('%Y-%m-%d')
    log_filename = name + ".log"
    logging.basicConfig(filename='./log/' + log_filename, filemode='a+', level=logging.DEBUG)
    try:
        ret = os.popen('ps nginx').readlines()
        if len(ret) < 2:
            logging.info(now.strftime('%H:%M:%S') + "error:programing error")
            time.sleep(3)
        else:
            logging.info(now.strftime('%H:%M:%S') + "running:programing running")
            time.sleep(3)
    except:
        logging.info(now.strftime('%H:%M:%S') + "error:"+sys.exc_info()[1])