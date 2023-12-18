# jellyfin 处理文件的脚本，用来解决文件名问题
# 去除[]符号以及不需要的内容

import os

BASE_NO_NEED = ['[', ']', '【', '】', '(', ')', '（', '）', '「', '」', '『', '』', '【', '】', '《', '》', '〈', '〉','HD1080','720p','1080p','x264','X264','x265','X265','AAC','AAC-iSCG','中英双字',
                '中英','国语','中字','国粤','双字','双语','BD','bd','1080P','720P','Mp4er','HD','English','english','CHS-ENG','CHS','bdys.me','BDYS','10bit','8bit','www.dygod.com','电影天堂',
                '.zwzm','压制','幻月','UHA-WINGS','BeanSub','HYSUB','sweetSub','JYFanSub','Airota&MakariHoshiyume','Amor','压制组','汉化组','Nekomoe kissaten','&','LoliHouse','内嵌','字幕',
                '简体','繁体','￡','小五','飘花','电影网','电影','www.domp4.cc','DMG','高清','4k','2k','4K','2K','标清','DVD','简繁','内封','WEB-DL','NetflixMKV','Netflix','更多','韩剧','美剧','电视剧','Video'
                ,'video','更多','www.','.com','piaohua','MP4dbmp4','小晓家园','xxjy.org','.org','精彩','资源','尽在', 'smk118',
                'mpand','蚂蚁仔','mayizai','学习增值好帮手','TVB','BBTV','资源','下载','阳光dygod','BTTV','剧集','打包','请访问']

def re_name(path):
    files=os.listdir(path)
    # print(files)
    for file in files:
        # print(file)
        # 去除权限用户文件夹
        if "S-1-5" in file or "re_name_jellyfin" in file or "System Volume Information" in file:
            print('跳过执行')
        else:
            if os.path.isdir(path + '/' + file):
                re_name(path + '/' + file)
            else:
                name = file 
                # print(name)
                for i in BASE_NO_NEED:
                    name = name.replace(i, '')
                # input_name=input("如果不需要此文件名，请输入文件名称，否则直接回车：")
                # if input_name:
                #     name=input_name
                # print(file)
                if name!=file:
                    print("更改后的名称为"+name)
                    os.rename(path + '/' + file, path + '/' + name)

if __name__ == '__main__':
    re_name('D:/')