# This file takes an input of adjacency lists which represent DAGs. The purpose
# of this algorithm is to find the longest path from node 0 and to display it.
import math 

# This fucntion is used to calculate and return the degrees of 
def degreesCalculation (graph):
    lengthOfGraph = len (graph)
    degrees = { }
    for index in range (0, lengthOfGraph):
        degrees [index] = 0
    for vertex in range (0, lengthOfGraph):
        for edge in graph[vertex]:
            degrees[edge] = degrees[edge] + 1
    return degrees

# This function is used to process the given graph through a topological
# sort algorithm which is to allow us to find the longest path.
def topoSort (unsortedGraph):
    sortedGraph = [ ]
    newList = [ ]
    degrees = degreesCalculation (unsortedGraph)
    degreesLength = len (degrees)
    for index in range (degreesLength):
        if degrees[index] == 0:
            newList.append(index)
    for item in newList:
        sortedGraph.append(item)
        if unsortedGraph[item] != 0:
            for nodes in unsortedGraph[item]:
                index = nodes
                degrees[index] = degrees[index] - 1
                if degrees[index] == 0:
                    newList.append(index)
    return sortedGraph

# This function takes the unsorted graph and sends it to the topoSort function
# to be sorted. It then calculates and prints the max distance for the DAG.
def findLongestPath(graph):
    distances = { }
    distances[0] = 0
    sortedGraph = topoSort(graph)
    for index in range(1, len(sortedGraph)):
        distances[index] = -math.inf
    for vertex in sortedGraph:
        for edge in graph[vertex]:
            if (distances[vertex] + 1) > distances[edge]:
                distances[edge] = distances[vertex] + 1
    try:
        maxDistance = 0
        for index in range(len(sortedGraph)):
            if maxDistance < distances[index]:
                maxDistance = distances[index]
        print(maxDistance)
    except:
        print (0)

# It is important to note that the first line before each list is the order of
# the DAG. Every input after the first is the list of adjacencies for the nodes from
# 0 to n - 1 of the DAG.
while True:
    unsortedGraph = { }
    newInput = int(input())
    if newInput != 0:
        for index in range(newInput):
            newInput = input()
            newInput = newInput.replace("\n", "")
            unsortedGraph[index] = list(map(int, newInput.split()))
        # Once we have the unsorted DAG we can send it through to be sorted.
        findLongestPath(unsortedGraph)
    else:
        break

