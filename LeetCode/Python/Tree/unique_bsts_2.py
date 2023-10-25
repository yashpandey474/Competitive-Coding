# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        def dfs(nums):
            if not nums:
                return [None]

            result = []
            for i in range(len(nums)):
                #ITH NUMBER IS ROOT
                leftGen = dfs(nums[:i])
                rightGen = dfs(nums[i + 1:])

                for l in leftGen:
                    for r in rightGen:
                        root = TreeNode(nums[i])
                        root.left = l
                        root.right = r
                        result.append(root)

            return result

        nums = list(range(1, n+1))
        return dfs(nums)

        
