#
# greedy.py
#
# This file provides a function implementing greedy best-first search for
# a route finding problem. Various search utilities from "route.py" are
# used in this function, including the classes RouteProblem, Node, and
# Frontier. Also, this function uses heuristic function objects defined
# in the "heuristic.py" file.
#
# YOUR COMMENTS INCLUDING CITATIONS
#
# YOUR NAME - THE DATE
#


from route import Node
from route import Frontier


def greedy_search(problem, h, repeat_check=False):
    """Perform greedy best-first search to solve the given route finding
    problem, returning a solution node in the search tree, corresponding
    to the goal location, if a solution is found. Only perform repeated
    state checking if the provided boolean argument is true."""

    # PLACE YOUR CODE HERE
    startNode = Node(problem.start, h_eval = h.h_cost(problem.start))

    if problem.is_goal(startNode.loc):
        return startNode
    
    #create priotiy que that sorts h cost
    myFrontier = Frontier(startNode, sort_by = 'h')
    reachedSet = set()
    reachedSet.add(startNode)

    while not myFrontier.is_empty():
        removedNode = myFrontier.pop()
        if problem.is_goal(removedNode.loc):
            return removedNode
        removedNodeList = removedNode.expand(problem, h_fun = h)
        for node in removedNodeList:
            if repeat_check == True:
                #if the child is not in the reached set
                if node not in reachedSet:
                    #add child to frontier
                    reachedSet.add(node)
                    #add child to the reached set
                    myFrontier.add(node)
            else:   
                myFrontier.add(node)
                
    return None
