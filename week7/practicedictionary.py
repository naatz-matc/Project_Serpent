#!/usr/bin/env python3

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
            print(f"Found Server:")
            print(f" Name         : {servers[server]['NAME']}")
            print(f" FQDN         : {servers[server]['FQDN']}")
            print(f" IP Address   : {servers[server]['IPADD']}")
    if not found:
        print ("Server not found")
