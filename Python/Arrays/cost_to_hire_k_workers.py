class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        start = 0
        end = len(costs)-1
        queue1 = []
        queue2 = []
        total_cost = 0
        while k:
            a = float('inf')
            b = float('inf')
            while len(queue1) < candidates and start<=end:
                heapq.heappush(queue1, costs[start])
                start+=1
            
            while len(queue2) < candidates and start<=end:
                heapq.heappush(queue2, costs[end])
                end-=1
                
            if queue1:
                a = queue1[0]
            if queue2:
                b = queue2[0]

            if a <= b:
                total_cost += a
                heapq.heappop(queue1)
            else:
                total_cost += b
                heapq.heappop(queue2)            
            
            k-=1

        return total_cost
