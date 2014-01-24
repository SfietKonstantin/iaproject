import socket
import struct
import sys
import os
import errno

def connect(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect(("192.168.0.2", 5555))
    except Exception as error:
        print("Connection error: ", error)
        sys.exit(-1)
    sock.setblocking(0)
    return sock
    
def getOrder(sock):
    try:
        order = sock.recv(3)
        return order
    except socket.error as error:
        err = error.args[0]
        if err == errno.EAGAIN or err == errno.EWOULDBLOCK:
            return None
        else:
            print("Connection error: ", error)
            sys.exit(-2)
    except Exception as error:
        print("Connection error: ", error)
        sys.exit(-2)

def send(sock, *messages):
    for message in messages:
        if isinstance(message, int):
            data = struct.pack('=B', message)
        else:
            data = message.encode('ascii')
            
        try:
            sock.send(data)
        except:
            print("Couldn't send message: ", data) 

def toInt(data):
    return struct.unpack('=B', data)[0]

def toString(data):
    return data.decode('ascii')