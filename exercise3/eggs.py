from sa import *
from numpy import *
from operator import attrgetter
from random import *

# checks if a state is legal
def is_legal(state, K, M, N):
    too_many_eggs = 0
    for x in state:
        eggs_in_row = 0
        for y in x:
            if y == 1:
                eggs_in_row+=1
                if eggs_in_row > K:
                    too_many_eggs += 1
    for x in state.transpose():
        eggs_in_column = 0
        for y in x:
            if y == 1:
                eggs_in_column += 1
                if eggs_in_column > K:
                    too_many_eggs += 1
    for i in range(-N+1,M-1):
        eggs_in_diagonal = 0
        for j in state.diagonal(i):
            if j:
                eggs_in_diagonal += 1
                if eggs_in_diagonal > K:
                    too_many_eggs += 1
    for i in range(-N+1,M-1):
        eggs_in_diagonal = 0
        for j in state[::-1].diagonal(i):
            if j:
                eggs_in_diagonal += 1
                if eggs_in_diagonal > K:
                    too_many_eggs += 1
    if too_many_eggs:
        return False
    return True
    
# problem specific implementation of SearchNode class
# sa.py
class EggSearchNode(SearchNode):
    # init method, sets M, N and K for the problem, and
    # initializes the neighbour list
    def __init__(self, state, M, N, K):
        self.M = M
        self.N = N
        self.K = K
        self.neighbours = []
        SearchNode.__init__(self, state)

    # generates neigbours of the node
    def generate_neighbours(self, F):
        for i,x in enumerate(self.state):
            for j,y in enumerate(x):
                new_state = self.state.copy() # copies the state of the current node

                # switches one bit
                if y == 0: 
                    new_state[i][j] = 1
                else:
                    new_state[i][j] = 0
                if is_legal(new_state, self.K, self.M, self.N):
                    # only if the new state is legal its F value is
                    # calculated and added to the neighbourlist
                    node = EggSearchNode(new_state, self.M, self.N, self.K)
                    node.F = F(node)
                    self.neighbours.append(node)
        # sort the neighbour list after F values
        self.neighbours.sort(key=attrgetter('F'))
        return self.neighbours.pop() # returns the greatest element in the list
                    
    # returns a random neighbour from the list
    def get_random_neighbour(self):
        return choice(self.neighbours)

# objective function, calculates the F value of the state
def F(node):
    eggs_placed = 0
    for x in node.state:
        for y in x:
            if y == 1:
                eggs_placed+=1
    return (1-1/(2*(eggs_placed or 1)))or 1 # to not get division by zero errors, the function returns just 1 if the value would be zero
    
# creates a start carton, empty with an egg in the top left corner.
def create_start_carton(M, N, K):
    state = zeros(M*N, dtype=int64).reshape(M,N)
    state[0][0] = 1
    return EggSearchNode(state, M, N, K)

# prints a given carton
def print_carton(carton):
    print(carton.state)

