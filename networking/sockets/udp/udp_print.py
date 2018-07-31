#!/usr/bin/env python3

from socket import socket, AF_INET, SOCK_DGRAM

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(("127.0.0.1", 5000))

# nc -v -u localhost 5000
while True:
    data, addr = sock.recvfrom(1024)
    print(data, addr)
