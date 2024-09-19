#!/usr/bin/python3

import socket

#setting timeout = s.settimeout() in seconds - will timeout if no response in amount of seconds specified
#cleaning up output - removing the b in ssh banner = convert into string first | strip data received using .strip()
def banner(ip, port):
    s = socket.socket()
    s.connect((ip, int(port)))
    s.settimeout(5)
    print(str(s.recv(1024)).strip('b'))

def main():
    ip - input("Please enter the IP: ")
    port = str(imput("Please enter the port: "))
    banner(ip, port)

main()
