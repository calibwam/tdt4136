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
                if y == 0 and self.F < self.M*self.N:
                    new_state[i][j] = 1
                else:
                    new_state[i][j] = 0
                node = EggSearchNode(new_state, self.M, self.N, self.K)
                node.F = F(node)
                self.neighbours.append(node)
        self.neighbours.sort(key=attrgetter('F'))
        return self.neighbours.pop()
                    
                

    def get_random_neighbour(self):
        return choice(self.neighbours)

def F(node):
    state = node.state
    eggs_placed = 0
    too_many_eggs = 0
    for i,x in enumerate(state):
        eggs_in_row = 0
        for j,y in enumerate(x):
            if y == 1:
                eggs_placed+=1
                eggs_in_row+=1
                if eggs_in_row > node.K:
                    too_many_eggs += 1
    for x in state.transpose():
        eggs_in_column = 0
        for y in x:
            if y == 1:
                eggs_in_column += 1
                if eggs_in_column > node.K:
                    too_many_eggs += 1
    for i in range(-node.N+1,node.M-1):
        eggs_in_diagonal = 0
        for j in state.diagonal(i):
            if j:
                eggs_in_diagonal += 1
                if eggs_in_diagonal > node.K:
                    too_many_eggs += 1
    for i in range(-node.N+1,node.M-1):
        eggs_in_diagonal = 0
        for j in state[::-1].diagonal(i):
            if j:
                eggs_in_diagonal += 1
                if eggs_in_diagonal > node.K:
                    too_many_eggs += 1
    return (eggs_placed - too_many_eggs/2)or 1
    
def create_start_carton(M, N, K):
    state = zeros(M*N, dtype=int64).reshape(M,N)
    state[0][0] = 1
    state[0][1] = 1
    return EggSearchNode(state, M, N, K)

def print_carton(carton):
    print(carton.state)


#print_carton(sa(create_start_carton(5,5,2),F,10,15,0.2))
print_carton(sa(create_start_carton(8,8,1),F,8,10,0.1))
