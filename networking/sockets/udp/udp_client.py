#!/usr/bin/env python3

from sys import exit
from socket import socket, AF_INET, SOCK_DGRAM, error

try:
    sock = socket(AF_INET, SOCK_DGRAM)
except error as e:
    exit("socket: {}".format(e))

HOST = "127.0.0.1"
PORT = 5000

while True:
    try:
        msg = input("Enter message: ")
    except EOFError as e:
        exit("\ninput: {}".format(e))

    try:
        sock.sendto(msg.encode(), (HOST, PORT))

        # note the lack of a bind statement, the socket is assigned an interface
        # and port by the operating system, which is used by other senders
        data, addr = sock.recvfrom(1024)
        print("Message[{}:{}] - {}".format(addr[0], addr[1], data.decode()))
    except error as e:
        exit("sendto/recvfrom: {}".format(e))
