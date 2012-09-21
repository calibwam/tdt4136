
class searchNode:
    def __init__(self, children, h, goal):
        self.children = children
        self.h = h
        self.opened = False
        self.goal = goal


def aStarSearch(startNode):
    closedSet = []
    agenda = [startNode]
    cameFrom = {}
    startNode.g = 0
    startNode.f = startNode.h + startNode.g

    for node in agenda:
        if node.goal:
            return node
        closedSet.append(agenda.pop(0))
        for child in node.children:
            if child not in closedSet:
                cameFrom[child] = node
                child.opened = True
                child.f = node.g+getDistance() + child.h
                child.parent = node
                agenda.append(child)
        agenda.sort(key=attrget('f'))

p = []
def reconstructPath(cameFrom, currentNode):
    if cameFrom[currentNode]:
        p.append(reconstructPath(cameFrom, cameFrom[currentNode])
        return [currentNode].append(p)
    else:
        return currentNode

def getHeuristicEstimate(node):
    return 1
