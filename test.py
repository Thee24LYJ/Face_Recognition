# -*- coding:utf-8 -*- 
"""
Author：G3
Time: 2021/6/30 
Software: PyCharm
"""
import cv2,requests
# # 发出http请求
# re = requests.get("http://192.168.137.230/control?var=framesize&val=9")
# # 查看响应状态
# print(re.status_code)
#
# url = r'http://192.168.137.230:81/stream'
cap = cv2.VideoCapture(0)
while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # 获取视频宽度
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    # 获取视频高度
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)  # 视频平均帧率
    print(frame_height,frame_width,fps)
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()