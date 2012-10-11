from sa import *

class EggSearchNode(SearchNode):
    def __init__(self, state, M, N, K):
        self.M = M
        self.N = N
        self.K = K
        self.neighbours = []
        SearchNode.__init__(self, state)

    def generate_neighbours(self, F):
        #TODO add F-evaluation
        for j, s in enumerate(self.state):
            for i,x in enumerate(s):
                new_state = self.state
                if x == 'X':
                    new_state[j][i] = '.'
                else:
                    new_state[j][i] = 'X'
                self.neighbours.append(EggSearchNode(new_state, self.M, self.N, self.K))

    def get_random_neighbour(self):
        return random.choice(self.neighbours)

def F(node):
    #TODO finish up F
    return 1

    
def create_start_carton(M, N, K):
    carton = []
    for i in range(M):
        string=[]
        for j in range(N):
            if j<K:
                string.append('X')
            else:
                string.append('.')
        carton.append(string)
    return EggSearchNode(carton, M, N, K)

def print_carton(carton):
    for s in carton.state:
        print("".join(s))


print_carton(sa(create_start_carton(6,6,1),F,10,10,0.1))
