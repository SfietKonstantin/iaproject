#!/usr/bin/python3

import socket, struct

# Try to connect 
try:
    sock.connect(("127.0.0.1", 5555))
except Exception as error:
    print("Connection error: ", error)

# Main event loop

