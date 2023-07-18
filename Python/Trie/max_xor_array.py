class Trie:
    def __init__(self):
        self.children = [None]*2
        

class Solution(object):
    def findMaxXor(self, number):
        current = self.root
        xor = 0

        for i in range(31, -1, -1):
            bit = (number >> i) & 1
            opposite = bit ^ 1

            if current.children[opposite] is None:
                current = current.children[bit]
            else:
                current = current.children[opposite]
                xor = xor | (1 << i)

        return xor
    def insertTrie(self, number):

        current = self.root
        for i in range(31, -1, -1):
            bit = (number >> i) & 1
            if current.children[bit] is None:
                current.children[bit] = Trie()
            current = current.children[bit]
        
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.root = Trie()
        #INSERT ALL IN TRIE
        for i in nums:
            self.insertTrie(i)

        #FOR EACH NUMBER; FIND MAXIMUM XOR
        max_xor = 0
        for i in nums:
            max_xor = max(max_xor, self.findMaxXor(i))


        #TAKE MAXIMUM OF ALL MAXIMUMS

        return max_xor

