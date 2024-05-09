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


def dijekstra(graph, n, start):
    distances = [float('inf')]*n
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        currDist, currNode = pq.pop()
        if currDist > distances[currNode]:
             continue
        
        for i in range(n):
            if graph[currNode][i] != 0:
                distance = graph[currNode][i]
                newDist = distance + currDist

                if newDist < distances[i]:
                    distances[i] = newDist
                    pq.append((newDist, i))
    return distances

dj = dijekstra(graph, v, 0)
print(dj)