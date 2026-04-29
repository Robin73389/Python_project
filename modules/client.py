#!/usr/bin/python3

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('10.188.180.116', 12345))
client_socket.send(b"Bonjour du client")
print(client_socket.recv(1024).decode())
client_socket.close()