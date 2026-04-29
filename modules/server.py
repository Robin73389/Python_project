#!/usr/bin/python3

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)
print("Ecouter sur le port 12345...")
conn,addr = server_socket.accept()
print("Connection from", addr)
print("CLient dit:", conn.recv(1024).decode())
conn.send(b"Bonjour depuis le serveur!")
conn.close()