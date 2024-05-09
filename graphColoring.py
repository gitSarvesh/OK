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
numColors = int(input("Enter the number of the colors you want : "))
for row in graph:
        print(row)

def isSafe(graph, v, colors, c):
    for i in range(len(graph)):
        if(graph[v][i]==1 and colors[i]==c):
            return False
    return True

def graphColoring(graph, n):
    colors = [-1]*n
    def colorVertex(v):
        if v==n:
             return True
        
        for c in range(numColors):
            if isSafe(graph, v, colors, c):
                colors[v] = c

                if colorVertex(v+1):
                     return True
                
                colors[v] = -1
        return False
    if not colorVertex(0):
         print("no solution")
         return
    
    print("Graph coloring solution")
    for i in range(n):
         print(f"Vertex {i+1}: Color {colors[i]+1}")

graphColoring(graph, v)