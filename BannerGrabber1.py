#!/usr/bin/python3

import socket

s = socket.socket()

#user to enter ip address and port | need to convert to string
ip = input("Please enter the IP: ")
port = str(input("Please enter the port: "))

#then convert back to integer
s.connect((ip, int(port)))

print(s.recv(1024))
