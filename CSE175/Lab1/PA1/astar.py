#
# astar.py
#
# This file provides a function implementing A* search for a route finding
# problem. Various search utilities from "route.py" are used in this function,
# including the classes RouteProblem, Node, and Frontier. Also, this function
# uses heuristic function objects defined in the "heuristic.py" file.
#
# YOUR COMMENTS INCLUDING CITATIONS
#
# YOUR NAME - THE DATE
#


from route import Node
from route import Frontier


def a_star_search(problem, h, repeat_check=False):
    """Perform A-Star search to solve the given route finding problem,
    returning a solution node in the search tree, corresponding to the goal
    location, if a solution is found. Only perform repeated state checking if
    the provided boolean argument is true."""

    # PLACE YOUR CODE HERE
    startNode = Node(problem.start, path_cost= 0.0, h_eval= h.h_cost(problem.start))

    if problem.is_goal(startNode.loc):
        return startNode
    
    #create priotiy que that sorts f cost
    myFrontier = Frontier(startNode, sort_by ='f')
    reachedSet = set()
    reachedSet.add(startNode)

    while not myFrontier.is_empty():
        removedNode = myFrontier.pop()
        if problem.is_goal(removedNode.loc):
            return removedNode
        removedNodeList = removedNode.expand(problem, h_fun = h)
        for node in removedNodeList:
            if repeat_check == True:
                #if child node is in the reached list
                if node in reachedSet:
                    #check if child is in frontier but with a higher cost
                   if myFrontier.contains(node) and (myFrontier[node] > node.value("f")):
                       #remove node from frontier
                        myFrontier.__delitem__(node)
                        #add the child node to the frontier
                        myFrontier.add(node)
                else:
                    #add child node to frontier
                    myFrontier.add(node)
                    #add child to reached set
                    reachedSet.add(node)
            else:   
                myFrontier.add(node)
    return None
