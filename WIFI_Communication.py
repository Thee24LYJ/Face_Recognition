# -*- coding:utf-8 -*- 
"""
Author：G3
Time: 2021/7/1 
Software: PyCharm
"""
import socket
import requests

def get_host_ip():
    """
    查询本机ip地址
    :return: ip
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    print("本地IP地址:",ip)
    return ip


def client_connect():
    # 创建 socket 对象
    serversocket = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)

    # 获取本地主机名
    host = get_host_ip()
    port = 8060

    # 绑定端口号
    serversocket.bind((host, port))

    # 设置最大连接数，超过后排队
    serversocket.listen(5)
    # 建立客户端连接
    clientsocket, addr = serversocket.accept()

    print("连接地址: %s" % str(addr))

    return clientsocket

def client_send(clientsocket,msg):
    msg = msg + "\r\n"
    clientsocket.send(msg.encode('utf-8'))

def client_close(clientsocket):

    clientsocket.close()
    print("连接断开")

def http_send(num,name,time):
    data={'num':num,'name':name,'time':time}
    re = requests.post("http://106.13.193.143:2404/persons", data=data)
    # print(re.status_code)
    # re = requests.get("http://106.13.193.143:2404/persons")
    # 查看响应状态
    if re.status_code == 200:
        print('send ok')
        # print(re.text)