import socket
import sys
import random
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 64
addr = (TCP_IP, TCP_PORT)
s = socket.create_server(addr)
s.listen(1)
random.seed()
secretNumber = random.randint(1,100)
conn, addr = s.accept()
print ("Connection address:", addr)
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    decodedMsg = data.decode()
    splitMsg = decodedMsg.split(" ")
    print ("data split:", splitMsg)
    if len(splitMsg) > 2:
        print ("wrong data, recieved more")
        conn.sendall("wrong data, recieved more".encode())
    else:
        if splitMsg[0] == "guess":
            if splitMsg[1].isdigit():
                if int(splitMsg[1]) < secretNumber:
                    conn.sendall("less".encode())
                elif int(splitMsg[1]) == secretNumber:
                    conn.sendall("correct!".encode())
                elif int(splitMsg[1]) > secretNumber:
                    conn.sendall("more".encode())
            else:
                print ("wrong data, not a digit")
                conn.sendall("wrong data, not a digit".encode())
        else:
            print ("wrong data, not guess")
            conn.sendall("wrong data, not guess".encode())
conn.close()
s.close()