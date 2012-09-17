
class searchNode:
    def __init__(self, children, h, goal):
        self.children = children
        self.h = h
        self.opened = False
        self.goal = goal


def aStarSearch(startNode):
    agenda = [startNode]
    startNode.g = 0
    startNode.f = startNode.h + startNode.g

    for node in agenda:
        if node.goal:
            return node
        for child in node.children:
            if child != node:
                child.opened = True
                child.f = node.g+getDistance() + child.h
                child.parent = node
                agenda.append(child)
        agenda.pop(0)
        agenda.sort(key=attrget('f'))



def getDistance():
    return 1
