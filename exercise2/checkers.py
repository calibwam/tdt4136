from astar import *

winState = 'rrrrr.bbbbb'

class CheckersSearchNode(SearchNode):
    def __init__(self, state):
        h = 1
        self.g = 1
        SearchNode.__init__(self, state, [],h,state==winState)
    
    def expandNode(self):
        space = self.state.find('.')
        for i, s in enumerate(self.state):
            if i+1 == space or i+2 == space or i-1 == space or i-2 == space:
                childState = list(self.state)
                color = self.state[i]
                childState[space] = color
                childState[i] = '.'
                childStateStr = "".join(childState)
                if childStateStr not in states:
                    self.children.append(CheckersSearchNode(childStateStr))


start = CheckersSearchNode('bbbbb.rrrrr')
result = aStarSearch(start)
#print(result)
for a in result:
    print(a)
