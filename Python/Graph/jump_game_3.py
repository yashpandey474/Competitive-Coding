class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        # BFS
        queue = [start]
        visited = set()

        while queue:
            curr = queue.pop(0)
            visited.add(curr)

            if arr[curr] == 0:
                return True

            next_indices = [curr - arr[curr], curr + arr[curr]]
            for i in next_indices:
                if 0 <= i < len(arr) and i not in visited:
                    queue.append(i)

        return False
            

            
