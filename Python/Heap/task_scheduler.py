class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:


        #CREATE MAP OF FREQUENCIES
        map_freq = {}
        for i in tasks:
            if i in map_freq:
                map_freq[i]+=1
            
            else:
                map_freq[i] = 1

        #ADD TO A HEAP
        heap = []
        for char, freq in map_freq.items():
            #ADD TO HEAP TO EXTRACT ONE WITH MAX FREQ
            heapq.heappush(heap, -freq)

        #WAITING HEAP
        heap_waiting = []
        time = 0
        while heap or heap_waiting:
            #CHOOSE ONE WITH HIGHEST FREQ
            if heap_waiting and time >= heap_waiting[0][0]:
                heapq.heappush(heap, heapq.heappop(heap_waiting)[1])
            time += 1
            if heap:
                freq = heapq.heappop(heap)
                #IF REMAINING FREQUENCY
                if -freq > 1:
                    heapq.heappush(heap_waiting, (time + n, freq + 1))

        return time

            
