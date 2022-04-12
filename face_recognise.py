# -*- coding: utf-8 -*-
import face_recognition
import cv2,datetime,requests
from read_data import read_name_list
from read_data import read_file
from WIFI_Communication import *


all_encoding, lable_list, counter = read_file('./dataset')
name_list = read_name_list('./dataset')
print(name_list)

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
name=""
base_url=r'http://192.168.137.192'

# 发出http请求  480*640
re = requests.get(base_url+'/control?var=framesize&val=8')
# 查看响应状态
if re.status_code==200:
    print('http ok')

# 读取摄像头，并识别摄像头中的人脸，进行匹配。
url = base_url+':81/stream'
video_capture = cv2.VideoCapture(url)
print('video finish')

# wifi连接
server = client_connect()
num1 = num2 = 0
n = 0
while video_capture.isOpened():

    ret, frame = video_capture.read()
    if ret:
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        # rgb_small_frame = small_frame[:, :, ::-1]
        if process_this_frame:
            face_locations = face_recognition.face_locations(small_frame)
            face_encodings = face_recognition.face_encodings(small_frame, face_locations)

            face_names = []
            name=""
            # 匹配，并赋值
            for face_encoding in face_encodings:
                i = 0
                j = 0
                for t in all_encoding:
                    for k in t:
                        match = face_recognition.compare_faces([k], face_encoding,tolerance=0.4)
                        if match[0]:
                            name = name_list[i]
                            j=1
                    i = i+1
                if j == 0:
                    name = "unknown"
                # print(name)
                face_names.append(name)

        process_this_frame = not process_this_frame
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0),  2)

            # cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), 2)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left+6, top-8), font, 1.0, (255, 255, 255), 1)
        cv2.imshow('Video', frame)
        if name!="":
            if name=="NAME":
                num1=num1+1
            if name=="unknown":
                num2=num2+1
            if num1 > 20:
                num1=0
                print(name)
                client_send(server, name)
                n = n + 1
                http_send(n,"名字", datetime.datetime.now())
            if num2 > 20:
                num2 = 0
                print(name)
                client_send(server, name)
                n = n + 1
                http_send(n, "未知人员", datetime.datetime.now())
        # print("回传:",str(server.recv(1024)))

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

client_close(server)
video_capture.release()
cv2.destroyAllWindows()
