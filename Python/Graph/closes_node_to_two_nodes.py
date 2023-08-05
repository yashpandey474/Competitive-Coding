class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def bfs(start):
            queue = []
            visited = set()
            distances = [float('inf')]*len(edges)
            distances[start] = 0
            queue.append((start, 0))

            while queue:
                current, dist = queue.pop(0)
                distances[current] = min(distances[current], dist)
                visited.add(current)

                if edges[current] != -1 and edges[current] not in visited:
                    queue.append((edges[current], dist + 1))
            return distances

        distances1 = bfs(node1)
        distances2 = bfs(node2)
        min_dist = float('inf')
        index = -1

        print(distances1)
        print(distances2)
        for i in range(len(edges)):
            if distances1[i] == -1 or distances2[i] == -1:
                continue
            if max(distances1[i], distances2[i]) < min_dist:
                min_dist = max(distances1[i], distances2[i])
                index = i

        return index
        
            
