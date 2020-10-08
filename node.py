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
        self.children.append(nodeToChild)

    def getChildren(self):
        return self.children

    def getParent(self):
        return self.parent

    def isGoalNode(self):
        return self.data.isGoal()

    def getNextNode(self):
        nextMove = self.data.getBestNeighbor()
        print("\nBest solution has Manhattan " + str(nextMove.getManhattan()))

        return nextMove

    def printCurrentNode(self):
        if(type(self) == None):
            print("Bad type for print")
        else:
            return self.data.printBoard()
    