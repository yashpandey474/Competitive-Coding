class MedianFinder:

    def __init__(self):
        #MAINTAIN A MIN-HEAP FOR GREATER ELEMENTS AND MAX-HEAP FOR SMALLER ELEMENTS
        self.small_heap = []
        self.large_heap = []

    def addNum(self, num: int) -> None:
        #SMALL HEAP IS EMPTY OR NUMBER IS SMALLER THAN LARGEST ELEMENT
        if not self.small_heap or -num >= self.small_heap[0]:
            heapq.heappush(self.small_heap, -num)
        #SMALL HEAP IS NOT EMPTY AND NUMBER IS LARGER THAN ITS LARGEST ELEMENT
        elif self.small_heap and -num < self.small_heap[0]:
            heapq.heappush(self.large_heap, num)

        #CHECK SIZES OF HEAPS
        if len(self.large_heap) > len(self.small_heap):
            if (len(self.large_heap) + len(self.small_heap))%2 == 0:
                #ADD TO SMALL HEAP; THE MIN ELEMENT FROM LARGE HEAP
                heapq.heappush(self.small_heap, -(heapq.heappop(self.large_heap)))

        if len(self.small_heap) > len(self.large_heap):
            if (len(self.large_heap) + len(self.small_heap))%2 == 0:
                #ADD TO LARGE HEAP; THE MAX ELEMENT FROM SMALL HEAP
                heapq.heappush(self.large_heap, -(heapq.heappop(self.small_heap)))
        


    def findMedian(self) -> float:

        #IF SIZES ARE EQUAL
        if len(self.small_heap) == len(self.large_heap):
            #GET MIN AND MAX
            maxEle = -self.small_heap[0]
            minEle = self.large_heap[0]

            return (minEle + maxEle)/2

        else:
            if len(self.small_heap) > len(self.large_heap):
                return -self.small_heap[0]
            else:
                return self.large_heap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
