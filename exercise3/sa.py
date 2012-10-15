# here be imports
import math # for math.exp
import random # for random.randoj

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
    P.F = F(P)
    T = T_max # sets the running temperature
    while True:
        if F(P) >= F_target:
            #the current node satifies as a solution
            return P
        
        P_max = P.generate_neighbours(F) # generate the neighbours, and returns the best one
        q = (P_max.F-P.F)/P.F # calculates q
        try:
            p = min(1, math.exp((-q)/T)) # calculates p, min of 1 and e^(-q/T)
        except OverflowError:
            p = 1
        x = random.random() # a random number between 0 and 1
        if x>p:
            # the random number is bigger than p, that is 
            # e^(-q/T) is lower than 1. Exploit a good lead
            P = P_max
        else:
            # explore random neighbours
            P = P.get_random_neighbour()
        T = T - dT # lower the temperature
