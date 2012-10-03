# implements the A* routine for the fraction problem
from astar import *

# the value we want the fraction to be
goal = 1/8

# subclass of SearchNode tailored to the Fraction problem
class FractionSearchNode(SearchNode):
    def __init__(self, state, level):
        h = 1 # the heuristic is just 1
        isGoal = int(state[:4])/int(state[4:]) == goal # if the first 4 values divided by the last 5 is equal to goal, we do have a goal node
        self.g = level # sets the g-value to the level of the node
        self.level = level #saves the level
        SearchNode.__init__(self, state, [], h, isGoal) # calls the super init method


    # implementationo of expandNode for the fraction problem
    def expandNode(self):
        if self.level < 9: # as the problem space has nine digits, the solution will be in the first nine levels neighbours from the start
            for i in range(len(self.state)): # loop through the state string to generate neighbours to it
                if i == self.level:
                    # if we are at the same place in the string as the level, there's no need to generate the child as it will be the same.
                    continue
                charAtLvl = self.state[self.level] # save the first character to swap
                charAtI = self.state[i] # save the second character to swap
                childState = list(self.state) # create a list copy of the parent state (because of immutable types)
                childState[self.level] = charAtI # swap
                childState[i] = charAtLvl
                s = "".join(childState) # create a string from the list
                if s not in states:
                    # if the state is not in already expanded states, add it to the list of children
                    # of the node
                    self.children.append(FractionSearchNode(s,self.level+1)) 

start = FractionSearchNode('138725496', 0)

print(aStarSearch(start))
