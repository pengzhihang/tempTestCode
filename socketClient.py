#coding:utf-8
import chardet
 
import socket               # 导入 socket 模块
 
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)         # 创建 socket 对象
host = '10.10.1.53' # 获取本地主机名
port = 6666                # 设置端口号
 
s.connect((host, port))

print type(s.recv(1024))
    
s.close()