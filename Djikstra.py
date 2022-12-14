''' 
 Siddesh Mishra
 Exp7:Djikstra Algorithm
 Roll no:06
'''
from collections import defaultdict
class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}
    def addNode(self,value):
        self.nodes.add(value)
    def addEdge(self, fromNode, toNode, distance):
        self.edges[fromNode].append(toNode)
        self.distances[(fromNode, toNode)] = distance

def dijkstra(graph, initial):
    visited = {initial : 0}
    path = defaultdict(list)
    nodes = set(graph.nodes)
    while nodes:
        minNode = None
        for node in nodes:
            if node in visited:
                if minNode is None:
                    minNode = node
                elif visited[node] < visited[minNode]:
                    minNode = node
        if minNode is None:
            break
        nodes.remove(minNode)
        currentWeight = visited[minNode]
        for edge in graph.edges[minNode]:
            weight = currentWeight + graph.distances[(minNode, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge].append(minNode) 
    return visited,path

customGraph = Graph()
n=int(input('Enter the number of nodes:'))
for i in range(n):
    nod=input('Enter node:')
    customGraph.addNode(nod)
e=int(input('\nEnter the number of edges:'))
for i in range(e):
    a=input('Enter from:')
    b=input('Enter to:')
    w=int(input('Enter cost:'))
    customGraph.addEdge(a,b,w)
s=input('\nEnter start node:')
print(dijkstra(customGraph, s))
