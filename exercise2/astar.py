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


def aStarSearch(startNode):
    closedSet = []
    agenda = [startNode]
    cameFrom = {}
    startNode.g = 0
    startNode.f = startNode.h + startNode.g

    for node in agenda:
        if node.goal:
            return node.state
#            return reconstructPath(cameFrom, node)
        closedSet.append(agenda.pop(0))
        node.expandNode()
        for child in node.children:
            if child not in closedSet:
                for n in agenda:
                    if child.state == n.state:
                        break
                cameFrom[child] = node
                child.opened = True
                child.f = node.g+getHeuristicEstimate(node) + child.h
                child.parent = node
                agenda.append(child)
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
