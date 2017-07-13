#!/usr/bin/env python

import socket


TCP_IP = '192.168.1.12'
TCP_PORT = 1013
BUFFER_SIZE = 1024
running = True
print "[*] tcpSender Started!"
print "[*] Connecting to", TCP_IP, "    Port:",TCP_PORT
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # s = New Socket
s.connect((TCP_IP, TCP_PORT)) # socket connect

while running:
    MESSAGE = raw_input("Enter Message to be sent: ")
    s.send(MESSAGE) # send message over socket
    data = s.recv(BUFFER_SIZE)
s.close()
print "received data: ", data