from os import *
from sys import *
from collections import *
from math import *

def maxPathValue(n, m, edges, values):
    # Write your code here.
    
    visited = set()
    def bfs(current_node, freq):

        visited.add(current_node)
        char = values[current_node - 1]

        if char not in freq:
            freq[char] = 0

        freq[char] += 1

        ans = max(freq.values())
        if current_node in graph:
            for v in graph[current_node]:
                if v in visited:
                    return -1
                if v not in visited:
                    ans = max(
                        ans,
                        bfs(v, freq.copy())
                    )

        visited.remove(current_node)

        return ans

    graph = {}
    for a, b in edges:
        if a not in graph:
            graph[a] = []

        graph[a].append(b)

    max_ans = -float('inf')
    for i in range(1, n+1):
        result = bfs(i, {})
        if result == -1:
            return -1
        max_ans = max(max_ans, result)

    return max_ans
