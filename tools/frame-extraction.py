# -*- coding:utf8 -*-
import cv2
import os
import shutil

def get_frame_from_video(video_name, interval, prefix="res", start_idx=0):
    save_path = video_name.split('.mp4')[0] + '/'
    is_exists = os.path.exists(save_path)
    if not is_exists:
        os.makedirs(save_path)
        print('path of %s is build' % save_path)
    else:
        shutil.rmtree(save_path)
        os.makedirs(save_path)
        print('path of %s already exist and rebuild' % save_path)

    video_capture = cv2.VideoCapture(video_name)
    i = 0
    j = start_idx - 1
 
    while True:
        success, frame = video_capture.read()
        i += 1
        if i % interval == 0:
            j += 1
            save_name = f"{prefix}_{str(j)}.jpg"
            cv2.imwrite(save_path + save_name, frame)
            print('image of %s is saved' % save_name)
        if not success:
            print('video is all read')
            break
 
if __name__ == '__main__':
    get_frame_from_video(
        video_name='open4.mp4',  # 输入视频路径
        interval = 3,                 # 采样间隔
        prefix="open",                 # 输出名称前缀
        start_idx=194                     # 输出编号起始位置
    )
