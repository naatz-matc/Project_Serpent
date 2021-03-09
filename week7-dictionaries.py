#!/usr/bin/env python3

#===Server IP Dictionary===============
ServerDictionary = {"server1.testlab.com" : "192.168.1.10"}
ServerDictionary["server2.testlab.com"] = "192.168.1.11"
ServerDictionary["server3.testlab.com"] = "192.168.1.12"
ServerDictionary["server4.testlab.com"] = "192.168.1.13"
ServerDictionary["server5.testlab.com"] = "192.168.1.14"
ServerDictionary["server6.testlab.com"] = "192.168.1.15"

servers = dict()

server1 = dict()
server1["NAME"] = "Server_1"
server1["FQDN"] = "server1.testlab.com"
server1["IPADD"] = "192.168.1.10"

server2 = dict()
server2["NAME"] = "Server_2"
server2["FQDN"] = "server2.testlab.com"
server2["IPADD"] = "192.168.1.11"

server3 = dict()
server3["NAME"] = "Server_3"
server3["FQDN"] = "server3.testlab.com"
server3["IPADD"] = "192.168.1.12"

server4 = dict()
server4["NAME"] = "Server_4"
server4["FQDN"] = "server4.testlab.com"
server4["IPADD"] = "192.168.1.13"

server5 = dict()
server5["NAME"] = "Server_5"
server5["FQDN"] = "server5.testlab.com"
server5["IPADD"] = "192.168.1.14"

server6 = dict()
server6["NAME"] = "Server_6"
server6["FQDN"] = "server6.testlab.com"
server6["IPADD"] = "192.168.1.15"

servers["server 1"] = server1
servers["server 2"] = server2
servers["server 3"] = server3
servers["server 4"] = server4
servers["server 5"] = server5
servers["server 6"] = server6

#===Listing of all FQDN's in Dictionary=====
print ("The FQDN's are:")
for key in sorted(ServerDictionary):
    print ("                ",key)
print ()

#===Listing of all IP Addresses=============
print ("The IP Addresses are:")
for value in sorted(ServerDictionary):
    print ("                " ,ServerDictionary[value])
print ()

#===Listing of all FQDN's & IP Address pairs===
print ("Server Dictionary:")
for server in ServerDictionary:
    print ("                ",server,"->",ServerDictionary[server])
print ()

#===Addition of two more Servers===============
ServerDictionary["server7.testlab.com"] = "192.168.1.16"
ServerDictionary["server8.testlab.com"] = "192.168.1.17"

server7 = dict()
server7["NAME"] = "Server_7"
server7["FQDN"] = "server7.testlab.com"
server7["IPADD"] = "192.168.1.16"

server8 = dict()
server8["NAME"] = "Server_8"
server8["FQDN"] = "server8.testlab.com"
server8["IPADD"] = "192.168.1.17"

servers["server 7"] = server7
servers["server 8"] = server8

#===Server Lookup in Dictionary===============
servers["server 1"] = server1
servers["server 2"] = server2
servers["server 3"] = server3
servers["server 4"] = server4
servers["server 5"] = server5
servers["server 6"] = server6
servers["server 7"] = server7
servers["server 8"] = server8

while True:
    found = False
    search = input("Server Search - Enter Server Name: ")

    if search.lower() == "done":
        print("closing program...")

        break
    for server in servers:
        if server == search.lower():
            found = True
            print("==============================================")
            print("Found Server")
            print(f"Name        : {servers[server]['NAME']}")
            print(f"FQDN        : {servers[server]['FQDN']}")
            print(f"IP Address  : {servers[server]['IPADD']}")
            print()
    if not found:
        print ("Server not found")
