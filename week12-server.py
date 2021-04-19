#!/usr/bin/env python3

import socket
# No data in quotes means this listens on all available interfaces
LHOST = ''

LPORT = 50007
RCV_DATA = ""

#This specifies that we are using IPv4 and are sending/receiving information as a stream
L_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
L_SOCK.bind((LHOST, LPORT))     #This is saying what do I want to listen on, binds the local host [LHOST] to a specific port [LPORt]

"""
This sets up what is essentialy an infinate loop. Since while(1) will always be true, the server will continue to listen for connection attempts from
 clients as long as the program is running and will accept those connection requests. The while 1: creates a seperate while loop inside of the while(1)
loop that once a connection is detected and accepted will continue to receive data in a stream untill there is no more. You need to specify how much data
to receive at a time in the L_CONN.recv() syntax. Once all the data is received, the break function will kick in and kick us out of the while 1: loop and
back out the while(1) 'infinate loop' and continues listening for new connections.
"""

while(1):
    L_SOCK.listen(1)
    L_CONN, addr = L_SOCK.accept()      #creates two different variables that can be called upon later instead of printing out a list
    print ('Connected by', addr)
    while 1:
        RCV_DATA = L_CONN.recv(1024)
        if not RCV_DATA: break
        print (f"The server received this data: {RCV_DATA}")
        # This line sends the data back to the client
        L_CONN.sendall(RCV_DATA)

    L_CONN.close()
