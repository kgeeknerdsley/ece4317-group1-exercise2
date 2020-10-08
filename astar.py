from puzzle import Puzzle
from node import Node
import time

# 0) Initialize: Assign starter Puzzle to Node
# 1) Check if node is goal node
#   1a) If goal node, stop! We found solution
#   1b) If not, generate the best next neighbor
# 2) Assign next neighbor to node
# 3) Set neighbor as current node, repeat to 1

#initialPuzzle = Puzzle([[0,1,3],[4,2,5],[7,8,6]])
#initialPuzzle = Puzzle([[1,2,3],[0,4,6],[7,5,8]])
initialPuzzle = Puzzle([[2,8,3],[1,6,4],[7,0,5]]) #Assignment start state
initialNode = Node(initialPuzzle, None, [])
foundSolution = False

currentNode = initialNode
boardsAttempted = 0

#start loop!
while(not foundSolution):
    currentNode.printCurrentNode()

    isGoal = currentNode.isGoalNode() #check if our current node is the solution

    if(isGoal): #if so, break out!
        print("Found solution! We outta here\n")
        print("Took " + str(boardsAttempted) + " attempts\n")
        currentNode.printCurrentNode()
        break

    nextNode = Node(currentNode.getNextNode(), currentNode, []) #next node is the best possible child
    currentNode.assignToChildren(nextNode)

    currentNode = nextNode
    boardsAttempted = boardsAttempted + 1

    #time.sleep(5)

    if(boardsAttempted == 40000):
        print("\nThis board is likely unsolvable!")
        break