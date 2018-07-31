#!/usr/bin/env python3

import sys
import struct
import socket

mc_group_name = "224.3.29.71"
serv_addr = ("", 5000)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(serv_addr)

group = socket.inet_aton(mc_group_name)
mreq = struct.pack("4sL", group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

while True:
    data, addr = sock.recvfrom(1024)
    print("Message[{}:{}] - {}".format(addr[0], addr[1], str(data)))
    print("Sending ack to[{}:{}]".format(addr[0], addr[1]))
    sock.sendto(b"ack", addr)
