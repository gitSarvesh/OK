v = int(input("Enter number of vertices : "))
e = int(input("Enter number of edges : "))
edges = []
graph = [[0] * v for _ in range(v)]
for _ in range(e):
    print("Enter Edges ")
    v1 = int(input("Enter edge between : "))
    v2 = int(input(" and between : "))
    e = int(input(" is : "))
    edges.append(e)
    graph[v1-1][v2-1] = e
    graph[v2-1][v1-1] = e

for row in graph:
        print(row)

print(edges)
edges.sort()
print(edges)

def krushkals(graph, edges, n):
    visited = []
    mst = []
    while len(visited)<n:
        i=0
        currEdge = edges[i]
        for j in range(n):
            # if j not in visited:
            #             visited.append(j)
            for k in range(j+1,n):
                if k not in visited and graph[j][k] == currEdge:
                     v11 = j
                     v22 = k
                     edge = (v11, v22)
                     mst.append(edge)
                     visited.append(k)
                     break
              
        i+=1
    print(visited)
    return mst      

mst = krushkals(graph, edges, v)   

for edge in mst:
     print(edge)