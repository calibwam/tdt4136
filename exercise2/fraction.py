from astar import *

class FractionSearchNode(SearchNode):
    def __init__(self, numerator, denominator, goal):
        state = [numerator, denominator]
        h = int(numerator)/int(denominator) - goal
    def __init__(self, state, children, h, goal):
