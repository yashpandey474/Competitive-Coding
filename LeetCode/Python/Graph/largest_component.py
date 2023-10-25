from math import gcd
def largestComponent(arr, n):
    #CREATE THE GRAPH
    graph = {i: [] for i in range(n)}

    for i in range(n):
        for j in range(i + 1, n):
            if gcd(arr[i], arr[j]) > 1:
                graph[i].append(j)
                graph[j].append(i)


    #FIND COMPONENT SIZES
    max_size = 1
    visited = set()

    def dfs(start):
        count = 1
        visited.add(start)

        for v in graph[start]:
            if v not in visited:
                count += dfs(v)

        return count


    for i in range(n):
        if i not in visited:
            max_size = max(max_size, dfs(i))

    return max_size

        
