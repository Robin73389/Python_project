#!/usr/bin/python3

import cv2
import socket
import numpy as np
import struct

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 12345))
server_socket.listen(1)
print("Ecouter sur le port 12345...")
conn,addr = server_socket.accept()
print("Connection from", addr)
print("CLient dit:", conn.recv(1024).decode())
conn.send(b"Bonjour depuis le serveur!")

image = cv2.imread('coco.jpg')

cv2.imshow('image exemple', image)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("manouvelleimage.jpg", image)


webcam = cv2.VideoCapture(0)

while(True):
    ret, frame = webcam.read()
    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
webcam.release()
cv2.destroyAllWindows()
conn.close()