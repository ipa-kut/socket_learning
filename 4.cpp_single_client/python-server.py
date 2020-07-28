#!/usr/bin/env python
## Must by Python 2 to send data, Python 3 only receives, Debug later if interested
import socket
import time

HOST = "127.0.0.1" # The server IP
PORT = 65432 # The same port as used by the server

print ("Starting Program")
count = 0
 
while (count < 1000):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT)) # Bind to the port 
    print("Listening")
    s.listen(5) # Now wait for client connection.
    c, addr = s.accept() # Establish connection with client.

    try:
        msg = c.recv(1024)
        print ("Received: ", msg)
        #time.sleep(1)   
        count = count + 1
        print ("The count is:", count)
        send_data = msg.decode() + str(count) + '\n'
        c.sendall(send_data.encode())
        print ("Sent {}".format(send_data))
        print ("")

    except socket.error as socketerror:
        print (count, " @socket failure")    
 
c.close()
s.close()

print ("Program finish")