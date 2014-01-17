#!/usr/bin/python3
import socket, struct

def send(sock, *messages):
    for message in messages:
        try:
            data = struct.pack('=B', message) if isinstance(message, int) else message
            sock.send(data)
        except:
            print("Couldn't send message: ", message)

# Try to connect 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.connect(("127.0.0.1", 5555))
except Exception as error:
    print("Connection error: ", error)

name = "Edward Team !!!"
send(sock, "NME", len(name), name)

# Main event loop

