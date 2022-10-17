import socket  # 创建TCP连接
from threading import Thread  # 多线程模块，进行多线程扫描
import time  # 时间模块，记录扫描所需时间


def main():
    portscan("106.13.194.65", 5555)


def portscan(target, port):
    # 1、定义portscan函数，进行TCP端口扫描
    try:
        client = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)  # 创建socket对象
        client.connect((target, port))  # 建立TCP连接
        while True:
            data = client.recv(1024)
            if not data: break
            print(repr(data))
            client.sendall(b'fuck you\r\n')
        client.close()
    except:
        pass  # 捕获异常


if __name__ == "__main__":
    main()
