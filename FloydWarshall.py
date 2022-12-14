import sys
INF = 999
 
def floydWarshall(graph):

    n = len(graph)
    dist = [[] for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            dist[i].append(graph[i][j])
     
    for k in range(n):
        print('\nD',k+1)
        for i in range(n):
            for j in range(n):               
                if dist[i][j] >dist[i][k]+dist[k][j]:
                    dist[i][j]=dist[i][k]+dist[k][j]
                    path[i][j]=k+1
                if dist[i][j]==INF:
                   print ("%7s" % ("INF"),end=' ')
                else:
                   print ("%7s" % (dist[i][j]),end=' ')
            print()
        print('P',k+1)
        for i in range(n):
            for j in range(n):
                print(path[i][j],end='  ')
            print()
 
R = int(input("Enter the number of vertices:"))

graph = []
path= []
print("Enter the entries for weight rowwise:")
for i in range(R):         
    a =[]
    for j in range(R):      
         a.append(int(input()))
    graph.append(a)
print("Enter the entries for path rowwise:")
for i in range(R):         
    a =[]
    for j in range(R):      
         a.append(int(input()))
    path.append(a) 

floydWarshall(graph)
