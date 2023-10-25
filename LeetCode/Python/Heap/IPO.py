class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        #TWO HEAPS

        #STORE PROFITS OF AVAILABLE PROJECTS
        max_heap = []

        #STORE CAPITAL OF UUNAVAIL PROJECTS
        min_heap = []

        for i in range(len(profits)):
            if capital[i] <= w:
                heapq.heappush(max_heap, (-profits[i], capital[i]))

            else:
                heapq.heappush(min_heap, (capital[i], profits[i]))

        #WHILE ELEMENTS IN MAX HEAP
        print(max_heap)
        print(min_heap)
        while max_heap and k > 0:
            prof, cap = heapq.heappop(max_heap)
            w = w - prof
            k-=1

            print('W = ', w)
            
            while min_heap and min_heap[0][0] <= w:
                c, p = heapq.heappop(min_heap)
                heapq.heappush(max_heap, (-p, c))

        return w

            
            
