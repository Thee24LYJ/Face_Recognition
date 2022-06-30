# 项目介绍

### 1.人脸图片获取
+ 运行```python face_detection.py```进行截取人脸图片
### 2.人脸识别
+ 运行```python face_recognise.py```进行人脸识别
>1.首先读取人脸图片进行训练并生成每个人对应的编码
>
>2.然后读取使用OpenCV读取ESP32-CAM传输的视频流信息进行人脸识别
>
>3.最后将人脸识别结果通过WIFI传输给STM32精英板进行边缘端数据处理，同时使用http网络请求将结果传输到云端并通过网页进行显示

# 文件说明
+ ```face_detection.py```文件用来获取待识别人脸图片
+ ```face_recognise.py```文件进行人脸识别及网络数据交互
+ ```WIFI_Communication.py```文件使用socket套接字与STM32精英板进行数据交互
+ ```camera.py```文件主要用来测试UDP传输，目前不需要使用
+ ```test.py```文件用来测试网络TCP传输和信令以及图片尺寸大小
+ ```read_data.py/read_img.py```用于读取dataset文件夹进行人脸数据训练

# 项目目录
```
Face_Recognition
│   camera.py
│   face_detection.py
│   face_recognise.py
│   README.md
│   read_data.py
│   read_img.py
│   test.py
│   WIFI_Communication.py
│
├───.idea
│   │   Face_Recognition.iml
│   │   misc.xml
│   │   modules.xml
│   │   workspace.xml
│   │
│   └───inspectionProfiles
│           profiles_settings.xml
│
├───dataset
│   ├───NAME
│   └───obma
│           obama.jpg
│
└───CameraWebServer
        CameraWebServer.ino
        app_httpd.cpp
        camera_index.h
        camera_pins.h
```
