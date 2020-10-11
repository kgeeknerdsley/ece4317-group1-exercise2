from puzzle import Puzzle
from node import Node
from collections import deque

#perform breadth first search!

# 1) Assign puzzle to node
# 2) Check if node is the goal node
#    2a) If it is, stop! We did it
#    2b) If not, generate children from the node
# 3) Place children into queue
#    3a) Before placing, set the child's parent property to the current node

initialPuzzle = Puzzle([[2,8,3],[1,6,4],[7,0,5]])
goalPuzzle = Puzzle([[1,2,3],[8,0,4],[7,6,5]])

print("\n Goal board")
goalPuzzle.printBoard()
print("\n Initial board")
initialPuzzle.printBoard()

isGoalPuzzle = False 

parentNode = Node(Puzzle([[]]),None,[])
node = Node(initialPuzzle,parentNode,[])     #root

visitedNodes = []                            # nodes visited in order 
queue = deque()                              # puzzles list to become nodes
queue.append(node.data)

clearList = [[],[],[]]

while (isGoalPuzzle == False): 

    node.data = queue.popleft()              # receives the first puzzle on the queue                                      
    node.parent = parentNode
    node.children = []                       # clear children from previous node
    visitedNodes.append(node)      

    if (node.data.isGoal()):                 # check if it is Goal Board !!!!!
        print("\n Found Goal Board: ")
        print(node.data.printBoard())
        isGoalPuzzle = True
        print("Number of visited Nodes:", len(visitedNodes))
        break            

    print("\n Node to be expanded: ")
    print(node.data.printBoard())

    childrenList = node.data.getNeighbors()

    for i in childrenList:
        for j in visitedNodes:                  # compare children puzzles to nodes.data visited
            if (i.getBoard() == j.data.getBoard()): 
                i.changeSelfBoard = clearList
               
        if(i.getBoard() != clearList ): 
            node.assignToChildren(i)            # give the children to its parent
            queue.append(i)                     # add on the queue of puzzles

    parentNode = node                           # give the previous node as a parent to the children node to be evaluated
     
   