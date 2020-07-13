#!/usr/bin/env python3
## Based on: https://realpython.com/python-sockets/

import socket

HOST = '192.168.56.3'  # The server's hostname or IP address.
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("Creating client with {}:{}".format(HOST,PORT))
    s.connect((HOST, PORT))
    i = 0
    while True:
        s.sendall(("Hello, world " + str(i)).encode())
        i += 1
        data = s.recv(1024)
        print('Received', repr(data.decode()))
