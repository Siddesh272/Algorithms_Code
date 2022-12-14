'''
Siddesh Mishra
SECMPNB1
Graph Colouring
'''
class Graph:
    # Constructor
    def __init__(self, edges, n):
        # A list of lists to represent an adjacency list
        self.adjList = [[] for _ in range(n)]
        # add edges to the undirected graph
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)
 
def isSafe(graph, color, v, c):
    # check the color of every adjacent vertex of `v`
    for u in graph.adjList[v]:
        if color[u] == c:
            return False
    return True
 
def kColorable(g, color, k, v, n):
    # if all colors are assigned, print the solution
    if v == n:
        print([COLORS[color[v]] for v in range(n)])
        return
    # try all possible combinations of available colors
    for c in range(1, k + 1):
        # if it is safe to assign color `c` to vertex `v`
        if isSafe(g, color, v, c):
            # assign color `c` to vertex `v`
            color[v] = c
            # recur for the next vertex
            kColorable(g, color, k, v + 1, n)
            # backtrack
            color[v] = 0
 
if __name__ == '__main__':
    edges = list(tuple(map(int,input().split()))
    for r in range(int(input('enter no of edges : ')))) 
    COLORS = ['', 'BLUE', 'GREEN', 'RED', 'YELLOW', 'ORANGE', 'PINK',
            'BLACK', 'BROWN', 'WHITE', 'PURPLE']
    n = int(input("Enter the number of vertices:"))
    g = Graph(edges, n)
    k = int(input("Enter the number of colours:"))
    color = [None] * n
    kColorable(g, color, k, 0, n)