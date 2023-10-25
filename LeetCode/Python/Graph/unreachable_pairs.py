class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:

        #FIND THE SIZES OF CONNECTED COMPONENTS
        component_sizes = []
        visited = set()
        graph = {i: [] for i in range(n)}

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node):
            size = 1
            visited.add(node)
            for i in graph[node]:
                if i not in visited:
                    size += dfs(i)

            return size

        for i in range(n):
            if i not in visited:
                component_sizes.append(dfs(i))

        #CALCULATE UNREACHABLE PAIRS
        total_pairs = 0
        for i in component_sizes:
            total_pairs += i * (n - i)

        return total_pairs // 2
