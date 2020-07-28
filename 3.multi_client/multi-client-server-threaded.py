#!/usr/bin/env python     
## Source: https://stackoverflow.com/questions/10810249/python-socket-multiple-clients                                                                                                                                                          

import socket               # Import socket module
import thread

def on_new_client(clientsocket,addr):
    count = 0
    while True:
        try:
            msg = clientsocket.recv(1024)
            #do some checks and if msg == someWeirdSignal: break:
            #print(addr, ' >> ', msg)
            msg = msg.decode() + " Server: " + str(count)
            count += 1
            #Maybe some code to compute the last digit of PI, play game or anything else can go here and when you are done.
            clientsocket.send(msg.encode())
        except socket.error as socketerror:
            print (count, " Lost connection to: ", addr)  
            clientsocket.close()
            return

s = socket.socket()         # Create a socket object
host = "127.0.0.1"          # Get local machine name
port = 65432                # Reserve a port for your service.

print 'Server started!'
print 'Waiting for clients...'

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Reuse address if already allocated. Useful if previous thread hung
s.bind((host, port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.

while True:
   c, addr = s.accept()     # Establish connection with client.
   print ('Got connection from', addr)
   thread.start_new_thread(on_new_client,(c,addr))
   #Note it's (addr,) not (addr) because second parameter is a tuple
   #Edit: (c,addr)
   #that's how you pass arguments to functions when creating new threads using thread module.
s.close()