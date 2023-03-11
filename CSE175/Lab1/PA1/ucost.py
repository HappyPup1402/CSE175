#
# ucost.py
#
# This file provides a function implementing uniform cost search for a
# route finding problem. Various search utilities from "route.py" are
# used in this function, including the classes RouteProblem, Node, and
# Frontier.
#
# YOUR COMMENTS INCLUDING CITATIONS
#
# YOUR NAME - THE DATE
#


from route import Node
from route import Frontier


def uniform_cost_search(problem, repeat_check=False):
    """Perform uniform cost search to solve the given route finding
    problem, returning a solution node in the search tree, corresponding
    to the goal location, if a solution is found. Only perform repeated
    state checking if the provided boolean argument is true."""

    # PLACE YOUR CODE HERE
    startLoc = Node(problem.start)

    if problem.is_goal(startLoc.loc):
        return startLoc
    
    #create priotiy que that sorts g cost
    myFrontier = Frontier(startLoc, sort_by='g')
    reachedNode = set()
    reachedNode.add(startLoc)
    
    while not myFrontier.is_empty():
        removedNode = myFrontier.pop()
        if problem.is_goal(removedNode.loc):
            return removedNode
        removdedNodeList = removedNode.expand(problem)
        for node in removdedNodeList:
            if repeat_check == True:
                if node in reachedNode:
                    #check if the child is in frontier and has a higher cost
                    if myFrontier.contains(node) and (myFrontier[node] > node.value(sort_by="g")):
                        #remove node from frontier
                        myFrontier.__delitem__(node)
                        #add child to the frontier
                        myFrontier.add(node)
                else:
                    #add child node to frontier
                    myFrontier.add(node)
                    #add child to reached set
                    reachedNode.add(node)
            else:   
                myFrontier.add(node)
    return None
