import socket

# 创建socket对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本机地址
host = socket.gethostname()
# 绑定端口号
server_socket.bind((host, 9999))
# 设置最大连接数，超过后排队
server_socket.listen(5)
while True:
    # 建立客户端连接
    client_socket, addr = server_socket.accept()
    print("连接地址为: %s" % str(addr))
    msg = "Hello World" + "\r\n"
    client_socket.send(msg.encode("utf-8"))
    client_socket.close()
