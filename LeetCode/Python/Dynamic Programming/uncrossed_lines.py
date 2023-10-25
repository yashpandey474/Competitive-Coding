class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:

        #CREATE A CACHE
        cache = {}

        #CREATE A DEPTH FIRST SEARCH FUNCTION
        def dfs(index1, index2):
            #OUT OF BOUNDS
            if index1 >= len(nums1) or index2>=len(nums2):
                return 0

            #ALREADY CACHED
            if (index1, index2) in cache:
                return cache[(index1, index2)]

            #SKIP AS DEFAULT
            res = 0

            # EQUAL CHARACTERS
            if nums1[index1] == nums2[index2]:
                    res = 1 + dfs(
                        index1 + 1,
                        index2 + 1
                    )
            #NON-EQUAL CHARACTERAS
            else:
                res = max(
                        dfs(index1 + 1, 
                        index2),
                        dfs(index1,
                        index2 + 1)
                )

            cache[(index1, index2)] = res
            return res

        return dfs(0, 0)
