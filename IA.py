import math

# We will do an algorithm based on auction.
# The fact is that the number of agents is 
# different over time, and that one agent 
# (a stack of wolves) can be splitted into
# two other wolves.
# 
# Our cost function is proportional to
# - ratio of creature / human
# - distance to a house
# - number of human to eat
# 
# We also have costs of splitting a stack
# of wolves into several stacks. This makes
# TODO

# Agent
# Represents a stack of creatures
# Have an utility function that maps
# to the distance of humans

crh = 1
s = 1

class Agent:
    i = -1
    j = -1
    count = -1
    def _ratioHuman(self, humanCount):
        return crh * math.exp(- math.pow((humanCount - self.count) / s, 2))
    
    def _distance(self, i, j, size):
        x = abs(self.i - i)
        y = abs(self.j - j)
        return 1 - (max(x, y) / size)
    def cost(self, humanCount, i, j, size):
        return self._ratioHuman(humanCount) * self._distance(i, j, size)
        


# Manager: 
# - gives autions
# - manage wolves etc
class Manager:
    pass
    #def 