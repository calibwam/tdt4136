from sa import *
from numpy import *
from operator import attrgetter
from random import *

class EggSearchNode(SearchNode):
    def __init__(self, state, M, N, K):
        self.M = M
        self.N = N
        self.K = K
        self.neighbours = []
        SearchNode.__init__(self, state)

    def generate_neighbours(self, F):
        for i,x in enumerate(self.state):
            for j,y in enumerate(x):
                new_state = self.state.copy()
                if y == 0:
                    new_state[i][j] = 1
                else:
                    new_state[i][j] = 0
                node = EggSearchNode(new_state, self.M, self.N, self.K)
                node.F = F(new_state)
                self.neighbours.append(node)
        self.neighbours.sort(key=attrgetter('F'))
        return self.neighbours.pop()
                    
                

    def get_random_neighbour(self):
        return choice(self.neighbours)

def F(state):
    #TODO finish F
    eggs_placed = 0
    for x in state:
        for y in x:
            if y == 1:
                eggs_placed+=1
    return eggs_placed or 1
    
def create_start_carton(M, N, K):
    state = zeros(M*N, dtype=int64).reshape(M,N)
    state[0][0] = 1
    return EggSearchNode(state, M, N, K)

def print_carton(carton):
    print(carton.state)


#print_carton(create_start_carton(6,6,1).state)
print_carton(sa(create_start_carton(5,5,2),F,10,10,0.1))
