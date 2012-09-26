from operator import attrgetter

class SearchNode:
    def __init__(self, state, children, h, goal):
        self.state = state
        self.children = children
        self.h = h
        self.opened = False
        self.goal = goal

    def expandNode(self):
        pass

states = {}
def aStarSearch(startNode):
    closedSet = []
    agenda = [startNode]
    states[startNode.state] = startNode
    cameFrom = {}
    startNode.g = 0
    startNode.f = startNode.h + startNode.g

    while agenda:
        node = agenda.pop(0)
        if node.goal:
            return node.state
#            return reconstructPath(cameFrom, node)
        closedSet.append(node)
        node.expandNode()
        for child in node.children:
            if child not in closedSet and child.state not in states:
                cameFrom[child] = node
                child.opened = True
                child.f = node.g+getHeuristicEstimate(node) + child.h
                child.parent = node
                agenda.append(child)
                states[child.state] = child
        agenda.sort(key=attrgetter('f'))

p = []
def reconstructPath(cameFrom, currentNode):
    if cameFrom[currentNode]:
        p.append(reconstructPath(cameFrom, cameFrom[currentNode]))
        return [currentNode].append(p)
    else:
        return [currentNode]

def getHeuristicEstimate(node):
    return 1
