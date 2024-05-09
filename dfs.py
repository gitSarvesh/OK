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

visited = [0]*v
queue = [0]
# def dfs(graph, n, start):
#     if(visited[start]==0):
#         visited[start] = 1
#     print(start+1, end=" ")
#     for i in range(n):
#         if graph[start][i]==1 and visited[i]==0:
#             dfs(graph, n, i)

# dfs(graph, v, 0)

def bfs(graph, n, start):
    
    visited[start] = 1
    while queue:
        current = queue.pop(0)
        print(current+1, end=" ")
        for i in range(n):
            if(graph[current][i]==1 and visited[i]==0):
                visited[i] = 1
                queue.append(i)

bfs(graph, v, 0)