#!/usr/bin/python3

import cv2
import socket
import zmq
import base64


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('10.188.180.116', 12345))
client_socket.send(b"Bonjour du client")
print(client_socket.recv(1024).decode())

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    buffer = cv2.imencode('.jpg', frame)
    jpg_as_text = base64.b64encode(buffer)
    socket.send(jpg_as_text)

cap.release()