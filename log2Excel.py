# coding:utf-8
import re
import xlwt
import sys
import time

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    # 更改此处
    f = open('a.log', 'r')
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
            reObj1 = re.compile('(>\S+|\s<)')
            temp_name = reObj1.findall(str(line))
            if temp_name !=[]:
                print "name:"+str(temp_name[0].decode('utf-8'))
                sheet.write(j, 1, str(temp_name[0].decode('utf-8')))
            else:
                print "_________________"
                sheet.write(j, 1, str("!"+str(line)))
            i += 1
        else:
            reObj2 = re.compile('(f\S+)')
            temp_url = reObj2.findall(str(line))
            print str(temp_url[0].decode('utf-8'))
            sheet.write(j, 2, str(temp_url[0].decode('utf-8')))
            j += 1
            i += 1

    workbook.save('DYTT.xls')