#!/usr/bin/env python3

import socket

hfile = open("ancient_latin.txt","r")
text_file = hfile.read()

RHOST = '127.0.0.1'
RPORT = 50007
SND_DATA = text_file

C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
C_SOCK.connect((RHOST, RPORT))
C_SOCK.send(bytearray(SND_DATA,'utf8'))

C_SOCK.close()
hfile.close()

