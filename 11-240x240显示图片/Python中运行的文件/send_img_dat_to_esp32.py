from socket import *

# 1. 创建socket
tcp_client_socket = socket(AF_INET, SOCK_STREAM)

# 2. 链接服务器
tcp_client_socket.connect(("192.168.0.16", 8080))

# 2. 打开文件，发送数据
with open(".\\text_img.dat", "rb") as f:
    for i in range(240):
        # 3.1 写到文件
        data = f.read(480)
        # 3.2 接收数据
        tcp_client_socket.send(data)  # 240*2=480 一行有240个点，每个点有2个字节

        print("发送第%d行" % (i + 1))
        # time.sleep(0.5)

print("发送完毕")

# 7. 关闭套接字
tcp_client_socket.close()
