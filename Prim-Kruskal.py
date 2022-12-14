'''
Siddesh Mishra
Exp4:Prims And Kruskals.
Roll no:06
'''
class Graph1:
    def __init__(self, num_of_nodes):
        self.m_num_of_nodes = num_of_nodes
        self.m_graph = [[0 for column in range(num_of_nodes)] 
                    for row in range(num_of_nodes)]
    def add_edge(self, node1, node2, weight):
        self.m_graph[node1][node2] = weight
        self.m_graph[node2][node1] = weight 
    def prims_mst(self):
        cost=0
        postitive_inf = float('inf')
        selected_nodes = [False for node in range(self.m_num_of_nodes)] 
        result = [[0 for column in range(self.m_num_of_nodes)] 
                      for row in range(self.m_num_of_nodes)]    
        indx = 0
        start = int(input('Enter start node:')) 
        while(False in selected_nodes):
           minimum = postitive_inf
           end = 0 
           for i in range(self.m_num_of_nodes):
             if selected_nodes[i]:
                for j in range(self.m_num_of_nodes):
                    if (not selected_nodes[j] and self.m_graph[i][j]>0):  
                        if self.m_graph[i][j] < minimum:
                            minimum = self.m_graph[i][j]
                            start, end = i, j
           selected_nodes[end] = True 
           result[start][end] = minimum 
           if minimum == postitive_inf:
               result[start][end] = 0
           indx += 1
           result[end][start] = result[start][end]
        for i in range(len(result)):
           for j in range(0+i, len(result)):
              if result[i][j] != 0:
                  print("%d - %d: %d" % (i, j, result[i][j]))
                  cost+=result[i][j]
        print('total cost:',cost)

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
    def kruskal_algo(self):
        result = []
        i, e = 0, 0
        cost= 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        for u, v, weight in result:
            print("%d - %d: %d" % (u, v, weight))
            cost+=weight
        print('Total cost:',cost)

option=int(input("1.Prims\n2.Kruskal's\n"))
n=int(input('Enter the number of nodes:'))
if(option==1):
    g=Graph1(n)
else: 
    g=Graph(n)
e=int(input('Enter the number of Edges:'))
for i in range(e):
    a=int(input('Enter from:'))
    b=int(input('Enter to:'))
    w=int(input('Enter weight:'))
    g.add_edge(a,b,w)
if(option==1):
    g.prims_mst()
else: 
    g.kruskal_algo()