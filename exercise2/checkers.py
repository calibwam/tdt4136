# implements the linear checkers problem instance of a star search
from astar import *

# the win state for the problem
winState = 'rrr.bbb'

# sub class of SearchNode for the linear checkers problem
class CheckersSearchNode(SearchNode):
    def __init__(self, state):
        h = 1 # set the h value
        self.g = 1 # set the g value
        SearchNode.__init__(self, state, [],h,state==winState) # call the super init method
    
    # implementing expandNode for the problem
    def expandNode(self):
        space = self.state.find('.') # find the space in the string
        for i, s in enumerate(self.state):
            if i+1 == space or i+2 == space or i-1 == space or i-2 == space: # if there is a legal move from the current  positition in the string, create a neighbour
                childState = list(self.state) # immutable stuff
                color = self.state[i] #find out which color w are
                childState[space] = color # do the swap
                childState[i] = '.'
                childStateStr = "".join(childState) # create string from the list
                if childStateStr not in states:
                    # if the state is not in the already explored states, add it to the children.
                    self.children.append(CheckersSearchNode(childStateStr))


start = CheckersSearchNode('bbb.rrr')
result = aStarSearch(start)
#print(result)
for a in result:
    print(a.state)
