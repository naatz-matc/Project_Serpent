#!/usr/bin/env python3

# Define the Dictionaries we will use. 
#BOOK1 = dict()
SERVER1 = {}
SERVER2 = dict()
SERVER3 = dict()
SERVER4 = dict()
SERVER5 = dict()
SERVER6 = dict()
ServerLibrary = dict()

# Create the first server
SERVER1['NAME'] = 'Server_1'
SERVER1['FQDN'] = 'server1.testlab.com'
SERVER1['IPADD'] = '192.168.1.10'

# Create the second server
SERVER2['NAME'] = 'Server_2'
SERVER2['FQDN'] = 'server2.testlab.com'
SERVER2['IPADD'] = '192.168.1.11'

# Create the third server
SERVER3['NAME'] = 'Server_3'
SERVER3['FQDN'] = 'server3.testlab.com'
SERVER3['IPADD'] = '192.168.1.12'

#create the fourth server
SERVER4['NAME'] = 'Server_4'
SERVER4['FQDN'] = 'server4.testlab.com'
SERVER4['IPADD'] = '192.168.1.13'

#create the fifth server
SERVER5['NAME'] = 'Server_5'
SERVER5['FQDN'] = 'server5.testlab.com'
SERVER5['IPADD'] = '192.168.1.14'

#create the sixth server
SERVER6['NAME'] = 'Server-6'
SERVER6['FQDN'] = 'server6.testlab.com'
SERVER6['IPADD'] = '192.168.1.15'

# Put the servers in the server library
# ============================
ServerLibrary = {"Server 1" : SERVER1, "Server 2" : SERVER2}
#ServerLibrary["Server 2" : SERVER2]
#ServerLibrary["Server 3" : SERVER3]
#ServerLibrary["Server 4" : SERVER4]
#ServerLibrary["Server 5" : SERVER5]
#ServerLibrary["Server 6" : SERVER6]

# What book are we looking for? test it with 'STAR WARS'
# ======================================================
while True:
    found = False
    serversearch = input("SERVER SEARCH - enter server name: ")

    if serversearch.lower() == 'done':
        print ("closing program...")

        break
    for SERVER in serversearch:
        if ServerLibrary == serversearch.lower():
            found = True
            print("====================================================")
            print("Found Server:")
            print(f"Name        : {ServerLibrary[SERVER]['NAME']}")
            print(f"FQDN        : {ServerLibrary[SERVER]['FQDN']}")
            print(f"IP Address  : {ServerLibrary[SERVER]['IPADD']}")

    if not found:
        print ("Server not found")
