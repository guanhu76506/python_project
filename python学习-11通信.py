socket_client:
from socket import socket, AF_INET, SOCK_STREAM

# 创建一个客户端的socket
from threading import Thread

client = socket(AF_INET, SOCK_STREAM)

con_address = ("localhost", 9001)
# 告诉客户端连接的服务器的IP和端口号
client.connect(con_address)



def send_msg(sock):
    while True:
        msg = input("输入要发送的消息")
        sock.send(msg.encode("utf-8"))


def recv_msg(sock):
    while True:
        data = sock.recv(512).decode("utf-8")
        if len(data) == 0:
            break
        print("收到了服务端的消息", data)


Thread(target=recv_msg, args=(client,)).start()
Thread(target=recv_msg, args=(client,)).start()

# client.send('狼来啦'.encode('utf-8'))
# client.close()



socket_server:
from socket import socket, AF_INET, SOCK_STREAM
# 创建socket对象
from threading import Thread

server = socket(AF_INET, SOCK_STREAM)

# 绑定端口号
server.bind(('', 9001))

# 开启监听状态
server.listen(5)


def send_msg(sock):
    while True:
        msg = input("输入要发送的消息")
        sock.send(msg.encode("utf-8"))


def recv_msg(sock):
    while True:
        data = sock.recv(512).decode("utf-8")
        if len(data) == 0:
            break
        print("收到了客户端的消息", data)


while True:
    sock, addr_info = server.accept()  # 阻塞的
    # print(socket,addr_info)
    t1 = Thread(target=send_msg, args=(sock,))
    t2 = Thread(target=recv_msg, args=(sock,))
    t1.start()
    t2.start()
    # data=sock.recv(1024).decode("utf-8")
    # print("{}发过来的消息是:{}".format(addr_info[0],data))

    # sock.close()
    print(addr_info, '离开了')







webserver:
from socket import socket, AF_INET, SOCK_STREAM
# 创建socket对象
from threading import Thread
import gevent
from gevent import monkey, socket

monkey.patch_all()

server = socket.socket()

# 绑定端口号
server.bind(('', 9001))

# 开启监听状态
server.listen(5)


def handle_client(sock):
    print('----------+++++')
    recv_data = sock.recv(1024).decode('utf-8')
    res_line = 'HTTP/1.1 200 OK\r\n'
    res_header = 'Content-Type:text/html,charset=utf-8\r\nServer:pythonServer\r\n'

    msg = '哈哈哈哈哈哈哈哈哈'
    response = res_line + res_header + "\r