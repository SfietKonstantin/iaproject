#!/usr/bin/python3
import sys
#import argparse
import Network
import Protocol
import Game
import time
import select

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
    socket = Network.connect("192.168.0.2", 5555)
    Protocol.setName(socket, name)
        
    # Main event loop
    data = bytes()
    while True:
        # Send commands
        if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            line = sys.stdin.readline()
            interpretCommand(line, socket)
        
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
launch("Edward")