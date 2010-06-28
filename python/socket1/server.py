import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 7777))
s.listen(5)

os.fork()
while True:
    conn, addr = s.accept()
    data = conn.recv(1024)
    print data
