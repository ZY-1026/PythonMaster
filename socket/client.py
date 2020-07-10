import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
s.connect((host, 9999))
msg = s.recv(1024)
s.close()
print(msg.decode("utf-8"))
