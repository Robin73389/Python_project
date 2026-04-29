#!/usr/bin/python3

import zmq
import cv2
import numpy as np
import base64
import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 12345))
server_socket.listen(1)
print("Ecouter sur le port 12345...")
conn,addr = server_socket.accept()
print("Connection from", addr)
print("CLient dit:", conn.recv(1024).decode())
conn.send(b"Bonjour depuis le serveur!")

socket.setsockopt_string(zmq.SUBSCRIBE, '')

while True:
    jpg_as_text = socket.recv()
    jpg_original = base64.b64decode(jpg_as_text)
    jpg_as_np = np.frombuffer(jpg_original, dtype=np.uint8)
    frame = cv2.imdecode(jpg_as_np, flag=1)

    cv2.imshow('Receiver', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()