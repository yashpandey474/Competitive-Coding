class Solution(object):
    def dfs(self, rooms, current):
        for i in rooms[current]:
            if i not in self.keys_set:
                self.keys_set.add(i)
                self.dfs(rooms, i)
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        self.keys_set = set()
        self.keys_set.add(0)
        self.dfs(rooms, 0)

        return len(self.keys_set) >= len(rooms)
