#!/usr/bin/env python3

import socket

LHOST = ''
LPORT = 50007
RCV_DATA = ""

L_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
L_SOCK.bind((LHOST, LPORT))

L_SOCK.listen(1)
L_CONN, addr = L_SOCK.accept()
print ('Connected by', addr)

RCV_DATA = L_CONN.recv(4096)

hFile = open("Secret_Message.txt","w")
hFile.write(RCV_DATA.decode('utf8'))
L_CONN.close()
hFile.close()
print (f"Output file <{hFile.name}> created successfully!!!")

#while(1):
#    L_SOCK.listen(1)
#    L_CONN, addr = L_SOCK.accept()
#    print ('Connected by', addr)
#    while 1:
#        RCV_DATA = L_CONN.recv(1024)
#        print (type(RCV_DATA))
#        RCV_DATA = str(RCV_DATA)
#        print (type(RCV_DATA))
#        print (RCV_DATA)
#        if not RCV_DATA: break
#    hFile.write(RCV_DATA)
#    print ("Message received. Output file created")
#    L_CONN.close()
#    hFile.close()
