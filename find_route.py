from collections import defaultdict
import math

fileName = input("Enter file name(ex: input1.txt) : ")

source = input("Enter Source: ")

destination = input("Enter Destination: ")


def Graph():
    dictionary = defaultdict(list)

    with open(fileName,'r') as file:

        for line in file:
            (parentNode,childNode,distance) = line.split()

            if parentNode == 'END' and childNode == 'OF' and distance == 'INPUT':
                break
            else :

              dictionary[parentNode].append(childNode)
              dictionary[childNode].append(parentNode)



    return  dictionary




#################DFS###########################

graph = Graph()

def dfs_path(graph,source,dest):
    result = []
    DFS(graph,source,dest,[],result)
    return result

def DFS(graph,source,dest,edge,result):
    edge+=[source]

    if source == dest:

        result.append(edge)

    elif(source != dest):

        for child in graph[source]:

            if child not in edge:

                DFS(graph,child,dest,edge[:],result)

dfsRoute = dfs_path(graph,source,destination)

if dfsRoute==[]:
    print("No route found")

else:
    print("Route Found")

############Dijkstra############

def graphForDijkstra():

    dictionary = defaultdict(dict)

    with open(fileName,'r') as file:
        for line in file:
            (parentNode,childNode,distance) = line.split()

            if parentNode == 'END' and childNode == 'OF' and distance == 'INPUT':
                break
            else :
                dictionary[parentNode][childNode] = int(distance)
                dictionary[childNode][parentNode] = int(distance)

    return  dictionary

graphForDijkstra = graphForDijkstra()

def dijkstra(graph,source , destination):

    unreachedNode = graph

    shortRoute = {}

    ancestor = {}

    infinite = math.inf

    route = []

    for node in unreachedNode:
        shortRoute[node] = infinite

    shortRoute[source] = 0



    while unreachedNode:
        lowNode = None

        for node in unreachedNode:

            if lowNode is None:

                lowNode = node

            elif shortRoute[node] < shortRoute[lowNode]:
                lowNode = node

        for childNode , edgeWeight in graph[lowNode].items():

            if edgeWeight+shortRoute[lowNode] < shortRoute[childNode]:

                    shortRoute[childNode] = edgeWeight+shortRoute[lowNode]

                    ancestor[childNode] = lowNode

        unreachedNode.pop(lowNode)


    if shortRoute[destination] != infinite:
        print("distance : " + str(shortRoute[destination]) + " km")

        currNode = destination

        while currNode is not None:
            try:
                route.insert(0, currNode)

                currNode = ancestor[currNode]

            except KeyError:
                break
        print("route : ")


        for edge in range(1,len(route)):
            print(route[edge-1] +" to "+ route[edge]+", "+str(shortRoute[str(route[edge])] - shortRoute[str(route[edge-1])])+" km")


    else :
         print("distance : infinity")
         print("route: none")



dijkstra(graphForDijkstra, source , destination)
