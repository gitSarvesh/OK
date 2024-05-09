v = int(input("Enter number of vertices : "))
e = int(input("Enter number of edges : "))

graph = [[0] * v for _ in range(v)]
for _ in range(e):
    print("Enter Edges ")
    v1 = int(input("Enter edge between : "))
    v2 = int(input(" and between : "))
    e = int(input(" is : "))
    graph[v1-1][v2-1] = e
    graph[v2-1][v1-1] = e

for row in graph:
        print(row)


def prims(graph, n, start):
    mst = []
    visited = []
    visited.append(start)

    while len(visited) < n:
        minEdge = None
        minCost = 999

        for i in range(n):
            for j in range(i+1,n):
                if j not in visited and graph[i][j] < minCost and graph[i][j]>0:
                    minEdge = (i, j)
                    minCost = graph[i][j]
        if minEdge:
            mst.append(minEdge)
            visited.append(minEdge[1])
    return mst

mst = prims(graph, v, 0)

for edge in mst:
     print(edge)