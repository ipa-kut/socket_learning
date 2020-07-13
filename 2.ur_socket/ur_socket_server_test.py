#!/usr/bin/env python
## Must by Python 2 to send data, Python 3 only receives, Debug later if interested
import socket
import time

HOST = "192.168.56.1" # The server IP
PORT = 30000 # The same port as used by the server

print ("Starting Program")
count = 0
 
while (count < 1000):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT)) # Bind to the port 
    s.listen(5) # Now wait for client connection.
    c, addr = s.accept() # Establish connection with client.

    try:
        msg = c.recv(1024)
        print ("Pose: ", msg)
        msg = c.recv(1024)
        print ("Joints: ", msg)
        msg = c.recv(1024)
        time.sleep(1)   
        if msg == "asking_for_data":
            count = count + 1
            print ("The count is:", count)
            time.sleep(0.5)
            time.sleep(0.5)
            send_data = "(200,50,45)" + '\n'
            c.send(send_data.encode())
            print ("Send 200, 50, 45")
            print ("")

    except socket.error as socketerror:
        print (count, " @socket failure")    
 
c.close()
s.close()

print ("Program finish")