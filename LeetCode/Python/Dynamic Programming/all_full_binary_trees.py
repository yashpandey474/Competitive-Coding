# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:

        cache = {0: [], 1: [TreeNode()]}

        #RETURN LIST OF FBT WITH N NODES
        def dfs(n):

            if n in cache:
                return cache[n]

            ans = []
            for l in range(n): #0 TO N - 1
                r = n - 1 - l
                leftTrees, rightTrees = dfs(l), dfs(r)

                for t1 in leftTrees:
                    for t2 in rightTrees:
                        root = TreeNode(left = t1, right = t2)
                        ans.append(root)


            cache[n] = ans
            return ans

        return dfs(n)
