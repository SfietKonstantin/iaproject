class Cell:
    human = 0
    vampires = 0
    werewolves = 0

class Game:
    n = -1
    m = -1
    board = []
    homeX = -1
    homeY = -1
    race = ""
    
    def init(self, n, m):
        self.n = n
        self.m = m
        self.board = []
        for i in range(n):
            column = []
            for j in range(m):
                column.append(Cell())
            self.board.append(column)
    def initHome(self, x, y):
        self.homeX = x
        self.homeY = y
        self.checkRace()
    
    def checkRace(self):
        if self.race == "":
            if self.homeX == -1 or self.homeY == -1:
                return
            cell = self.board[self.homeY][self.homeX]
            if cell.vampires > 0:
                self.race = "V"
            elif cell.werewolves > 0:
                self.race = "W"
    
    def setHuman(self, x, y, count):
        self.board[y][x].human = count
 
    def setVampire(self, x, y, count):
        self.board[y][x].vampires = count
        self.checkRace()
        
    def setWerewolf(self, x, y, count):
        self.board[y][x].werewolves = count
        self.checkRace()
    
    def getHuman(self):
        human = []
        for i in range(self.n):
            for j in range(self.m):
                cell = self.board[i][j]
                if cell.human > 0:
                    human.append({"coord": (i, j), "count": cell.human})
        return human
    
    def getCreatures(self):
        creatures = []
        for i in range(self.n):
            for j in range(self.m):
                cell = self.board[i][j]
                if self.race == "V" and cell.vampires > 0:
                    creatures.append({"coord": (i, j), "count": cell.vampires})
                if self.race == "W" and cell.werewolves > 0:
                    creatures.append({"coord": (i, j), "count": cell.werewolves})
        return creatures
    
    def __str__(self):
        race = "?"
        if self.race != "":
            race = self.race
        
        returnedData = "My race: %s\n" % race
        separator = ("-" * (6 * self.m + 1)) 
        for i in range(self.n):
            returnedData += separator + "\n"
            for j in range(self.m):
                returnedData += "|"
                cell = self.board[i][j]
                returnedData += "%i,%i,%i" % (cell.human, cell.vampires, cell.werewolves)
            returnedData += "|\n"
        returnedData += separator
        return returnedData
                
                
                
                