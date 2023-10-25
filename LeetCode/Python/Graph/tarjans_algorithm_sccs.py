def stronglyConnectedComponents(n, edges):
    # Write your code here

    #CREATE GRAPH
    graph = {i: [] for i in range(n)}

    for a, b in edges:
        graph[a].append(b)

    #CREATE REQUIRED ARRAYS
    disc = [-1]*n
    low = [-1]*n
    stack_member = [False]*n
    stack = []
    time = 0
    def dfs(node):
        nonlocal time
        #SET DISCOVERY TIME
        disc[node] = time
        low[node] = time
        #INCREMENT TIME
        time += 1
        #MARK AS IN STACK
        stack_member[node] = True
        stack.append(node)

        #EXPLORE NEIGHBORS
        for v in graph[node]:
            #UNVISITED NEIGHBOR
            if disc[v] == -1:
                dfs(v)
                low[node] = min(low[node], low[v])

            elif stack_member[v]:
                low[node] = min(low[node], disc[v])

        #FOUND HEAD OF SCC
        w = -1
        if low[node] == disc[node]:
            while w != node:
                w = stack.pop()
                print(w, end = " ")
                stack_member[w] = False

            print()
    #EXPLORE FOR ALL UNVISITED NODES
    for i in range(n):
        if disc[i] == -1:
            dfs(i)
t = int(input())
for i in range(t):
    v, e = map(int, input().split())
    edges = []
    for j in range(e):
        a, b = map(int, input().split())
        edges.append([a, b])

    stronglyConnectedComponents(v, edges)

quit()
