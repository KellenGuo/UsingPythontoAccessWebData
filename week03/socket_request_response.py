"""In this assignment you write a Python program to retrieve a web page over a socket and display the headers from the web server.
http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0
"""

import socket

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.connect(("www.pythonlearn.com", 80))

"""Add Host:www.pythonlearn.com to solve <Direct IP access not allowed> issue"""
cmd = "GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\r\nHost: www.pythonlearn.com\r\n\r\n".encode()
mySocket.send(cmd)

while True:
    data = mySocket.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
    
mySocket.close()