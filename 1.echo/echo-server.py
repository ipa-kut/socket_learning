#!/usr/bin/env python3
## Based on: https://realpython.com/python-sockets/

import socket

HOST = '192.168.56.1'  #  IP that the server shall be using. Clients look for this. localhost = 127.0.0.1
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Reuse address if already allocated. Useful if previous thread hung
    print("Creating server with {}:{}".format(HOST,PORT))
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print("Got: ", data.decode())
            conn.sendall((data.decode() + " response").encode())


# netstat -an |grep 127.0.0.1     : shows socket state
# lsof -i -n  |grep 127.0.0.1     : shows socket state
# telnet <HOST> <PORT>            : open a socket connection in terminal for transceving


