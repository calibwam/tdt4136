from operator import attrgetter

# class for the searchnode. needs a method for expanding it implemented.
class SearchNode:
    def __init__(self, state, children, h, goal):
        self.state = state
        self.children = children
        self.h = h
        self.opened = False
        self.goal = goal

    def expandNode(self):
        pass

# global hasmap to be able to see if a state has been used, and thus you do not need to 
# generate already visisted nodes
states = {}

# the a star search routine. 
#       * startNode - the node you will start from

def aStarSearch(startNode):
    # create the agenda, add the state of the startnode to the states and create a hasmap
    # for the paths. Also sets the g value for the starnode and calculates the f value
    agenda = [startNode]
    states[startNode.state] = startNode
    cameFrom = {}
    startNode.g = 0
    startNode.f = startNode.h + startNode.g
    
    # the main search loop
    while agenda:
        node = agenda.pop() # take the best node from the agenda
        if node.goal:
            # we've found a goal, and starts to construct the path to return it
            return reconstructPath(cameFrom, node)
        # the node is not a goal, we expand it by generating neighbours
        node.expandNode()
        for child in node.children:
            if child.state not in states:
            # if we've expanded this state before, we do not need to consider putting it into the agenda
                cameFrom[child] = node # add the node to the path hashmap
                child.opened = True # we have opened the node
                child.f = node.g+distance_to_goal_esitmate(node) + child.h # calculate the f value
                child.parent = node # the child has has the current node as parrent
                agenda.append(child) # add the child to the agenda
                states[child.state] = child # add the state of the child to the state map
        agenda.sort(key=attrgetter('f'), reverse=True) # sort the agenda after f values, and reverse it so we can use pop()


# reconstructs the path to get to a given node
#       * cameFrom    - hashmap of parents-childs
#       * currentNode - the node we will construct the path from
def reconstructPath(cameFrom, currentNode):
    if currentNode in cameFrom:
        path = reconstructPath(cameFrom, cameFrom[currentNode])
        path.insert(0,cameFrom)
        return path
    else:
        return [currentNode]


# gives an estimate from the given node to the goal an action will give. if the problem needs another
# estimate than 1, it has to be reimplemented.
def distance_to_goal_esitmate(node):
    return 1
