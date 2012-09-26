from astar import *

goal = 1/4

class FractionSearchNode(SearchNode):
    def __init__(self, state, level):
        h = 1
        isGoal = int(state[:4])/int(state[4:]) == goal
        self.g = level
        self.level = level
        SearchNode.__init__(self, state, [], h, isGoal)


    def expandNode(self):
        if self.level < 9:
            for i in range(len(self.state)):
                if i == self.level:
                    continue
                charAtLvl = self.state[self.level]
                charAtI = self.state[i]
                childState = list(self.state)
                childState[self.level] = charAtI
                childState[i] = charAtLvl
                print(self.level+1)
                self.children.append(FractionSearchNode("".join(childState),self.level+1))

start = FractionSearchNode('138725496', 0)

print(aStarSearch(start))
