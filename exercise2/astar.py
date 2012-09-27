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
    agenda = [startNode]
    states[startNode.state] = startNode
    cameFrom = {}
    startNode.g = 0
    startNode.f = startNode.h + startNode.g

    while agenda:
        node = agenda.pop()
        if node.goal:
            #return node.state
            return reconstructPath(cameFrom, node)
        node.expandNode()
        for child in node.children:
            if child.state not in states:
                cameFrom[child] = node
                child.opened = True
                child.f = node.g+getHeuristicEstimate(node) + child.h
                child.parent = node
                agenda.append(child)
                states[child.state] = child
        agenda.sort(key=attrgetter('f'), reverse=True)


def reconstructPath(cameFrom, currentNode):
    if currentNode in cameFrom:
        path = reconstructPath(cameFrom, cameFrom[currentNode])
        path.insert(0,cameFrom)
        return path
    else:
        return [currentNode]

def getHeuristicEstimate(node):
    return 1
