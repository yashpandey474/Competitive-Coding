class Solution:

    def __init__(self, nums: List[int]):
        self.og = nums
        self.n = len(nums)
        

    def reset(self) -> List[int]:
        return self.og
        

    def shuffle(self) -> List[int]:
        arr = self.og[:]
        for i in range(self.n - 1, -1, -1):
            rand = random.randint(0, i)
            arr[i], arr[rand] = arr[rand], arr[i]
            
        return arr
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
