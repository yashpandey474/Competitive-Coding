# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        if not root:
            return result



        def dfs(root, answer, current):
            #REACHED A LEAF ROOT
            if not root.left and not root.right:
                #OBTAINED TARGET SUM
                current += root.val
                answer += [root.val]
                if current == targetSum:
                    result.append(answer)

                return

            #NON-NONE NODE
            if root.left:
                dfs(root.left, answer + [root.val], current + root.val)
            if root.right:
                dfs(root.right, answer + [root.val], current + root.val)


        dfs(root, [], 0)
        return result


            
