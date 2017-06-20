# coding:utf-8
import re
import xlwt
import sys
import time

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    # 更改此处
    f = open('./Data/Mp4.data', 'r')
    workbook = xlwt.Workbook(encoding='utf-8')
    sheet = workbook.add_sheet('test', cell_overwrite_ok=True)
    i = 1
    j = 1
    for line in f.readlines():
        line.strip()
        print "正在读"+str(i)+"行"
        print line
        # time.sleep(0.5)
        print "正在写第"+str(j)+"行"
        if i % 2 == 1:
            print "name:"+str(line.decode('utf-8'))
            sheet.write(j, 0, str(line.decode('utf-8')))
            i += 1
        else:
            print str(line.decode('utf-8'))
            sheet.write(j, 1, str(line.decode('utf-8')))
            j += 1
            i += 1

    workbook.save('Mp4.xls')