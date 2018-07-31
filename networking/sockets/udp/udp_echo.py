#!/usr/bin/env python3

from sys import exit
from socket import socket, AF_INET, SOCK_DGRAM, error

HOST = ""
PORT = 5000

try:
    sock = socket(AF_INET, SOCK_DGRAM)
except error as e:
    # an integer argument is used as the return code, any other object is
    # printed to stderr with a return code of 1
    #
    # note format() calls the __format__() method of its arguments, this often
    # calls the __str__() method on the object in question
    exit("socket: {}".format(e))

try:
    sock.bind((HOST, PORT))
except error as e:
    exit("bind: {}".format(e))

while True:
    data, addr = sock.recvfrom(1024)
    print("Message[{}:{}] - {}".format(addr[0], addr[1], data.decode()))
    reply = "ok: " + data.decode()
    sock.sendto(reply.encode(), addr)

sock.close()
