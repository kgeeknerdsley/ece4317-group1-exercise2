#Class definition for the node structure
#Nodes hold a puzzle object as their data, and link to children of different puzzles

class Node:
    def __init__(self,puzzleData,parentNode,childrenNodes):
        self.data = puzzleData #type Puzzle
        self.parent = parentNode #type Node
        self.children = childrenNodes #type List, of different Puzzle objects, since it can have more than 2 children

    def assignParent(self, parentNode):
        pass

    def assignToChildren(self, nodeToChild):
        pass

    def getChildren(self):
        return self.children

    def getParent(self):
        return self.parent