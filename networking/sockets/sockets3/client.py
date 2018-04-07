#!/usr/local/bin/python3

import socket

# connect to 127.0.0.1:50007
HOST = "localhost"
PORT = 50007

# ipv4 tcp socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT)) # connect to remote host
    s.sendall(b"Hello world") # send byte string
    data = s.recv(1024) # recieve response
print("Recieved..." + str(data))
