import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 5005
addr=(TCP_IP, TCP_PORT)
BUFFER_SIZE = 64
s = socket.create_connection(addr)
while 1:
    guess = input("guess the number: ")
    s.sendall(guess.encode())
    data = s.recv(BUFFER_SIZE)
    if data:
        dataDecoded=data.decode()
        print ("server response: ", dataDecoded)
        if dataDecoded=="correct!":
            print ("congratualtions! you won!")
            break
    else: 
        print ("damaged data recieved, exiting")
        break
s.close()

