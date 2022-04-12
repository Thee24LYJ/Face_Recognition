# -*- coding:utf-8 -*- 
"""
Author：G3
Time: 2021/6/19 
Software: PyCharm
"""
import os
import cv2
import sys

pathname = r"./dataset/NAME/"
i = 0


# 视频采集,检测人脸并截取图片
def Video_capture(window_name, camera_idx, catch_pic_num):
    cv2.namedWindow(window_name)

    # 视频来源，可以来自一段已存好的视频，也可以直接来自摄像头
    cap = cv2.VideoCapture(camera_idx)

    # 告诉OpenCV使用人脸识别分类器
    classfier = cv2.CascadeClassifier(
        r"E:\Anaconda3\pkgs\libopencv-3.4.2-h20b85fd_0\Library\etc\haarcascades\haarcascade_frontalface_alt2.xml")

    # 识别出人脸后要画的边框的颜色，RGB格式
    color = (0, 255, 0)

    while cap.isOpened():
        ok, frame = cap.read()  # 读取一帧数据
        if not ok:
            break

            # 将当前帧转换成灰度图像
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 人脸检测，1.2和2分别为图片缩放比例和需要检测的有效点数
        faceRects = classfier.detectMultiScale(grey, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
        if len(faceRects) > 0:  # 大于0则检测到人脸
            Video_face_capture(cap, catch_pic_num, pathname)
            for faceRect in faceRects:  # 单独框出每一张人脸
                x, y, w, h = faceRect
                cv2.rectangle(frame, (x - 10, y - 10), (x + w + 10, y + h + 10), color, 2)

        # 显示图像
        cv2.imshow(window_name, frame)
        c = cv2.waitKey(10)
        if c & 0xFF == ord('q'):
            break
            # 释放摄像头并销毁所有窗口
    cap.release()
    cv2.destroyAllWindows()


# 获取人脸图像
def Video_face_capture(capture, catch_pic_num, path_name):
    global i
    flag, frame = capture.read()
    if i < catch_pic_num:
        if flag == True:
            i = i + 1
            filename = "image" + str(i) + ".jpg"
            print(filename)
            if not os.path.exists(path_name):
                os.makedirs(path_name)
            cv2.imwrite(path_name + str(i) + ".jpg", frame, [cv2.IMWRITE_JPEG_CHROMA_QUALITY, 100])  ##命名 图片 图片质量


if __name__ == '__main__':
    # url为esp32cam视频采集端的ip地址
    url = r'http://192.168.137.192:81/stream'

    if len(sys.argv) != 1:
        print(r"Usage:%s camera_id\r\n" % (sys.argv[0]))
    else:
        Video_capture("face_detection", url, 10)
