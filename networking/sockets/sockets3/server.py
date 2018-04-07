#!/usr/local/bin/python3 

import socket 

HOST = "" # all available network interfaces
PORT = 50007 # server port 

# AF_INET (ipv4)
# SOCK_STREAM (tcp)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
    s.bind((HOST, PORT)) # bind to local port 
    s.listen(1) # accept clients
    conn, addr = s.accept() # blocks until client connects
    with conn: 
        print("Connected with client... " + str(addr))
        while True:
            data = conn.recv(1024) # read client data (1024 byte buffer)
            if not data: break
            conn.sendall(data) # echo data back
