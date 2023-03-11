#
# bfs.py
#
# This file provides a function implementing breadth-first search for a
# route-finding problem. Various search utilities from "route.py" are
# used in this function, including the classes RouteProblem, Node, and
# Frontier.
#
# YOUR COMMENTS INCLUDING CITATIONS
#
# YOUR NAME - THE DATE
# Izaac Ramirez - 10/4/2022
#Logic discussed with Rodrigo Martinez


from route import Node
from route import Frontier


def BFS(problem, repeat_check=False):
    """Perform breadth-first search to solve the given route finding
    problem, returning a solution node in the search tree, corresponding
    to the goal location, if a solution is found. Only perform repeated
    state checking if the provided boolean argument is true."""

    # PLACE YOUR CODE HERE
    startNode = Node(problem.start)

    #checks if starting node is the goal
    if problem.is_goal(startNode.loc): 
        return startNode
    
    #initialize frontier and add the starting node
    myFrontier = Frontier(startNode, True)
    
    #initialize the reached set and add the starting nde
    reachedSet = set () 
    reachedSet.add(startNode)
    
    while not myFrontier.is_empty():
        removedNode = myFrontier.pop()
        
        #if the node contains goal than return removed node
        if problem.is_goal(removedNode.loc):
            return removedNode
        
        #expand the node to get a list of its child
        removedNodeList = removedNode.expand(problem)
        for node in removedNodeList:
            if repeat_check == True:
                if node not in reachedSet:
                    reachedSet.add(node)
                    myFrontier.add(node)
            else:
                myFrontier.add(node)
    return None
