#!/usr/bin/python3

import socket

#setting timeout = s.settimeout() in seconds - will timeout if no response in amount of seconds specified
def banner(ip, port):
    s = socket.socket()
    s.connect((ip, int(port)))
    s.settimeout(5)
    print(s.recv(1024))

def main():
    ip - input("Please enter the IP: ")
    port = str(imput("Please enter the port: "))
    banner(ip, port)

main()
