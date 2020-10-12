from puzzle import Puzzle
from node import Node
from queue import Queue
import pydot
import graphviz

#perform breadth first search!

# 1) Assign puzzle to node
# 2) Check if node is the goal node
#    2a) If it is, stop! We did it
#    2b) If not, generate children from the node
# 3) Place children into queue
#    3a) Before placing, set the child's parent property to the current node

initialPuzzle = Puzzle([[2,8,3],[1,6,4],[7,0,5]]) #Assignment start state
initialNode = Node(initialPuzzle, None, [])
foundSolution = False

currentNode = initialNode
childrenToCheck = Queue() #to test new puzzles, in order of creation
generatedNodes = [Puzzle([[2,8,3],[1,6,4],[7,0,5]])] #a list to remember everything we made, to avoid duplicates
visitedNodes = [] #a list of everything we visited
alreadyMade = False

graph = pydot.Dot(graph_type='graph',format='png')  #set up a blank graph

while(not foundSolution):
    if(currentNode.isGoalNode()): #if we find the solution
        print("Found the goal node!")
        currentNode.printCurrentNode()
        break
    
    nextMoves = []
    nextMoves = currentNode.generateNextMoves() #gets list of possible moves to make

    parentNodeGraph = pydot.Node(currentNode.getBoardString()) #remember our parent node for 

    nextMoveIndex = 0

    #for everything in the next move list...
    #test the move against all the other generated ones
    for i in nextMoves:
        alreadyMade = False

        for x in generatedNodes:
            if(i.boardsEqual(x.getBoard())): #if the board we made matches a board we already made, ignore it from the list
                alreadyMade = True
        #print("Children in level " + str(level) + " :")
        #i.printBoard()

        if(not alreadyMade): #if no duplicate found...
            childNodeGraph = pydot.Node(i.printBoardString()) #add new node to graph
            graph.add_edge(pydot.Edge(parentNodeGraph,childNodeGraph)) #link parent and this node

            generatedNodes.append(i) #add to list of generated nodes, since it's the first one


            childrenToCheck.put(Node(i,currentNode,None)) #place into queue to check next
            nextMoveIndex = nextMoveIndex + 1 #to iterate over list numerically
    
    nextNode = childrenToCheck.get() #pop off the top of the queue
    visitedNodes.append(currentNode) #we visited this one!
    currentNode = nextNode #new current node
    
graph.write("part2b") #generate final graph. run in graphviz with | dot -Tpng part2b -o outfile.png