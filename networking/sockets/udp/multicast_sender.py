#!/usr/bin/env python3

import sys
import struct
import socket

msg = b"she sells sea shells by the seashore"
mc_group = ("224.3.29.71", 5000)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(0.5)

ttl = struct.pack("b", 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

try:
    n = sock.sendto(msg, mc_group)

    while True:
        try:
            data, addr = sock.recvfrom(1024)
            print("Message[{}:{}] - {}".format(addr[0], addr[1], str(data)))
        except socket.timeout as e:
            print("read timedout", file=sys.stderr)
            break;
finally:
    sock.close()
