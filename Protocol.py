import Network
import IA

def setName(socket, name):
    Network.send(socket, "NME", len(name), name)
    
class ByeException(Exception):
    pass
    
def manageOrder(socket, order, game):
    orderStr = Network.toString(order)
    print("Received order %s" % orderStr)
    if orderStr == "SET":
        n = Network.toInt(socket.recv(1))
        m = Network.toInt(socket.recv(1))
        game.init(n, m)
    elif orderStr == "HUM":
        # Passing: legacy rule
        # Only reading data from socket
        n = Network.toInt(socket.recv(1))
        for k in range(n):
            x = Network.toInt(socket.recv(1))
            y = Network.toInt(socket.recv(1))
    elif orderStr == "HME":
        x = Network.toInt(socket.recv(1))
        y = Network.toInt(socket.recv(1))
        game.initHome(x, y)
    elif orderStr == "MAP" or orderStr == "UPD":
        n = Network.toInt(socket.recv(1))
        for k in range(n):
            x = Network.toInt(socket.recv(1))
            y = Network.toInt(socket.recv(1))
            h = Network.toInt(socket.recv(1))
            v = Network.toInt(socket.recv(1))
            w = Network.toInt(socket.recv(1))
            game.setHuman(x, y, h)
            game.setVampire(x, y, v)
            game.setWerewolf(x, y, w)
        print(game)
        print("================")
        human = game.getHuman()
        creatures = game.getCreatures()
        for creature in creatures:
            agent = IA.Agent()
            agent.i = creature["coord"][0]
            agent.j = creature["coord"][1]
            agent.count = creature["count"]
            print("Agent: %s" % str(creature["coord"]))
            for h in human:
                print("Human: %s. %f" % (str(h["coord"]), agent.cost(h["count"], h["coord"][0], h["coord"][1], game.n)))
            
        
        
        
    elif orderStr == "END":
        pass
        #ici on met fin à la partie en cours
        #Réinitialisez votre modèle
    elif orderStr == "BYE":
        raise ByeException()
    
