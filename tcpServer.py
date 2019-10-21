import socket
import sys

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 64
addr = (TCP_IP, TCP_PORT)
s = socket.create_server(addr)
s.listen(1)

conn, addr = s.accept()
print ("Connection address:", addr)
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print ("received data:", data.decode())
    conn.sendall(data)  # echo
conn.close()