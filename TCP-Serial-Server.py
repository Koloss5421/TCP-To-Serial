#!/usr/bin/env python

import socket
import serial
import time

TCP_IP = '192.168.1.2'
TCP_PORT = 2001
BUFFER_SIZE = 1024
running = True

print "[*] TCP To Serial Server Started!"
print "[*] Setting up write to COM Port!"
ser = serial.Serial('COM2')
time.sleep(5)
print "[*] Setting up Listener:", TCP_IP, "     Port:", TCP_PORT
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
while running:
    print "[*] Listening..."
    s.listen(1)
    conn, addr = s.accept()
    print '[+] Connection Received: ', addr
    while 1:
        data = conn.recv(BUFFER_SIZE)
        if not data: break
        print "[+] Received Data: ", data
        print "[-] Writing Data to Com Port..."
        ser.write(data.encode('utf-8'))
        ser.flush()
        break
ser.close()
conn.close()