# 自动截取视频的随机一帧作为封面

import os
import random
import cv2

BASE_NO_NEED = ['mp4','avi','mkv']

def capture_frame(video_path, frame_num, output_path):
    # 创建一个VideoCapture对象
    cap = cv2.VideoCapture(video_path)
    # 设置要获取的帧号
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
    # 读取帧
    ret, frame = cap.read()
    # 如果读取成功，保存该帧为图片
    if ret:
        print('save图片: ', output_path)
        # 中文路径存在问题
        # success = cv2.imwrite(output_path, frame)
        # if success:
        #     print(f"Frame saved successfully to {output_path}")
        # else:
        #     print(f"Failed to save frame to {output_path}")
        # 使用流的方式进行读取
        cv2.imencode('.jpg', frame)[1].tofile(output_path)
    # 释放VideoCapture对象
    cap.release()

def re_poster(path):
    files=os.listdir(path)
    # print(files)
    for file in files:
        # print(file)
        # 去除权限用户文件夹
        if "S-1-5" in file or "re_name_jellyfin" in file or "System Volume Information" in file:
            print('跳过执行')
        else:
            if os.path.isdir(path + '/' + file):
                re_poster(path + '/' + file)
            else:
                name = file 
                print(name)
                for i in BASE_NO_NEED:
                    if i in name:
                        img_name = name.replace(('.'+i),'')+"-poster.jpg"
                        print("海报图片是："+img_name)
                        capture_frame(path + '/' + file, random.randrange(200,3000), path + '/' + img_name)

if __name__ == '__main__':
    re_poster('D:/')