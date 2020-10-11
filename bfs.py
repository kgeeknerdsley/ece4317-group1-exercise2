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

#Assignment
initialPuzzle = Puzzle([[2,8,3],[1,6,4],[7,0,5]])
goalPuzzle = Puzzle([[1,2,3],[8,0,4],[7,6,5]])

# TEST CASES to show it can find the goalPuzzle.
'''initialPuzzle = Puzzle([[1,2,3],[4,5,6],[7,0,8]])
goalPuzzle = Puzzle([[1,2,3],[4,5,6],[7,8,0]])'''

#ANOTHER TEST (supposed to find goal at loop 137)
'''initialPuzzle = Puzzle([[2,3,8],[1,6,4],[7,0,5]])
goalPuzzle = Puzzle([[1,2,3],[4,0,8],[7,6,5]])'''


print("\n Goal board")
goalPuzzle.printBoard()
print("\n")
print("\n Initial board")
initialPuzzle.printBoard()
print("\n")

isGoalPuzzle = False 

listPuzzle = []                         
listPuzzle.append(initialPuzzle)

visitedPuzzle = []                       

tempPuzzle = Puzzle([[],[],[]])
clearList = [[],[],[]]

i = 0

while (isGoalPuzzle == False):
    
    tempPuzzle = listPuzzle.pop(0)
    
    print("Puzzle being expanded:")  
    print(tempPuzzle.printBoard()) 
    print("\n")

    if (tempPuzzle.isGoal()):                           #check if board is the goal one, if yes break the loop
        print("\n Found Goal board :")
        print(tempPuzzle.printBoard())
        isGoalPuzzle = True
        visitedPuzzle.append(tempPuzzle)
        print("Number of visited Puzzles:", len(visitedPuzzle))
        break 
    
    visitedPuzzle.append(tempPuzzle)

    childrenList = tempPuzzle.getNeighbors()             # generate children 

    for j in childrenList:
        for z in visitedPuzzle:
            if (j.getBoard() == z.getBoard()):
                #print("ENTERED")                         #check if it is entering at least once 
                j.changeSelfBoard(clearList)
                         
        
        if( j.getBoard() != clearList):
            listPuzzle.append(j)    
   
    i = i + 1
    
    #print(i)
    #print(" List Puzzle size:")
    #print(len(listPuzzle))
    

    



