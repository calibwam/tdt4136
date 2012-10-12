import math
import random

# the main abstract search node class
class SearchNode:
    # super init method, takes a state and stores it,
    # to be called by subclass' init method
    def __init__(self, state):
        self.state = state # the state of the node

    # generate each neighbour of the current node,
    # does not need to be a legal solution. It is up
    # to subclass to store the neigbours
    def generate_neighbours(self, F):
        pass

    # returns a randomly selected neighbour of the node
    def get_random_neighbour(self):
        pass


# the main search function.
# Arguments:
#   
#       - start_node:       the first node to evaluate (subclass of SearchNode)
#       - F         :       the objective function (returns int)
#       - F_target  :       the value of an optimal goal state (int)
#       - T_max     :       the starting temperature (int)
#       - dT        :       amount the temperature should fall with (int)
#
def sa(start_node, F, F_target, T_max, dT):
    P = start_node # stores the start node in P
    T = T_max # sets the running temperature
    while True:
        if F(P.state) >= F_target:
            #the current node satifies as a solution
            return P
        
        P_max = P.generate_neighbours(F)
        q = (F(P_max.state)-F(P.state))/F(P.state)
        p = min(1, math.exp((-q)/T))
        x = random.random()
        if x>p:
            P = P_max
        else:
            P = P.get_random_neighbour()
        T = T - dT
