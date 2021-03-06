#!/usr/bin/python3
import sys
#import argparse
import Network
import Protocol
import Game
import IA
import time
import threading
import queue

def startThread(t, q):
    t = threading.Thread(target=readInput, args=(sys.stdin, t, q))
    t.daemon = True
    t.start()

def readInput(stream, thread, queue):
    line = input()
    queue.put(line)
    startThread(thread, queue)

def interpretCommand(text, socket):
    print("Interpreting %s" % text)
    splittedText = text.split(",")
    if splittedText[0] == "MOV":
        if len(splittedText) != 6:
            return
        x = int(splittedText[1])
        y = int(splittedText[2])
        
        count = int(splittedText[3])
        
        newX = int(splittedText[4])
        newY = int(splittedText[5])
        
        Network.send(socket, "MOV", 1, x, y, count, newX, newY)
    
    if splittedText[0] == "ATK":
        if len(splittedText) != 3:
            return
        x = int(splittedText[1])
        y = int(splittedText[2])
        
        Network.send(socket, "ATK", x, y)

def launch(name):
    # Game
    game = Game.Game()
    
    # Try to connect 
    socket = Network.connect("192.168.0.3", 8080)
    Protocol.setName(socket, name)
    
    # Thread for inputs
    q = queue.Queue()
    t = None
    startThread(t, q)
    
        
    # Main event loop
    data = bytes()
    while True:
        # Send commands
        try:  
            line = q.get_nowait()
            interpretCommand(line, socket)
        except queue.Empty:
            pass
        
        # Get order
        order = Network.getOrder(socket)
        
        try:
            if order is not None:
                Protocol.manageOrder(socket, order, game)
        except Protocol.ByeException:
            break    
    
    socket.close()
    

#parser = argparse.ArgumentParser(description='VvsW')
#parser.add_argument('name', metavar='name', type=str, nargs=1,
                    #help='Name of the bot')
#args = parser.parse_args()
#name = args.name[0]
launch("Not Edward")