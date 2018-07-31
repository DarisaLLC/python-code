#!/usr/bin/env python3

import time
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

sock.bind(("", 5000))
data = b"UDP talker is saying things"

while True:
    sock.sendto(data, ("<broadcast>", 5001))
    time.sleep(1)
