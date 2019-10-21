import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 5005
addr=(TCP_IP, TCP_PORT)
BUFFER_SIZE = 64
msg = "Hello, World!"
MESSAGE =msg.encode()
s = socket.create_connection(addr)
s.sendall(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()

print ("received data:", data.decode())