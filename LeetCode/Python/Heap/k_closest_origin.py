class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        heap = []

        for i in points:
            distance = i[0]*i[0] + i[1]*i[1]
            if len(heap) < k:
                heapq.heappush(heap, (-distance, i[0], i[1]))

            else:
                if distance < -heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (-distance, i[0], i[1]))
        ans = [[heap[i][1], heap[i][2]] for i in range(len(heap))]

        return ans 
