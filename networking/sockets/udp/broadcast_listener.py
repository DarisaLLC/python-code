import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.bind(("0.0.0.0", 5001))

while True:
    data, addr = sock.recvfrom(1024)
    print("Message[{}:{}] - {}".format(addr[0], addr[1], data))
