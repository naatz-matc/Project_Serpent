#!/usr/bin/env python3

import socket

RHOST = '127.0.0.1'
RPORT = 50007
SND_DATA_1 = 'I FINALLY got this part of the assignment to work! HORRAY!!!!!' '\n'
SND_DATA_2 = 'I will be on a trip this comming week where I WILL NOT have internet accesss' '\n'
SND_DATA_3 = 'Would it be alright to get an extension on the lab assignment(s) for Week 13??' '\n'
RCV_DATA = ""

#Creating a list for setting up the loop the assignment asked for:
DATA_LIST = [SND_DATA_1, SND_DATA_2, SND_DATA_3]

#This is needed to specify that the IP protocol being used is IPv4 and to send/receive information as a stream
C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#This line establishes a connection to the server with the specified IP address and port number
C_SOCK.connect((RHOST, RPORT))

#The loop the assignment asked for. Same explanation as below, just set up in a loop for less lines of code
for DATA in DATA_LIST:
    C_SOCK.send(bytearray(DATA,'utf8'))

#This line will convert whatever format the variable SND_DATA is in into a byte array, otherwise there will be an error message
#when you try to send this data to the server or other specified target machine
#C_SOCK.send(bytearray(SND_DATA_1,'utf8'))
#C_SOCK.send(bytearray(SND_DATA_2,'utf8'))
#C_SOCK.send(bytearray(SND_DATA_3,'utf8'))

#This line allows the sending machine (client) to receive information from other sources and stores it in the variable RCV_DATA, with the argument in
#parenthesis on how many bytes to receive before dropping anything additonal

RCV_DATA = C_SOCK.recv(1024)

#This line with the .decode will print the received data and format it into UTF-8 format, no matter how the other machine sent out the information
print (RCV_DATA.decode('utf8'))

C_SOCK.close()
