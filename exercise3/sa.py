import math
import random

class SearchNode:
    def __init__(self, state):
        self.state = state

    def generate_neighbours(self, F):
        pass

    def get_random_neighbour(self)
        pass


def sa(start_node, F, F_target, T_max, dT):
    P = start_node
    T = T_max
    while True:
        if F(P) >= F_target:
            #the current node is a good solution
            return P
        
        P_max = P.generate_neighbours(F)
        q = (F(P_max)-F(P))/F(P)
        p = min(1, math.exp((-q)/T))
        x = random.random()
        if x>p:
            P = P_max
        else:
            P = P.get_random_neighbour()
        T = T - dT
