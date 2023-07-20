# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        #QUEUE FOR LEVEL ORDER TRAVERSAL
        queue = []
        #STORE MAX WIDTH
        max_width = 0

        #PUSH ROOT: INDEX = 0
        queue.append((root, 1))

        #WHILE QUEUE IS NOT EMPTY
        while queue:
            #HAVE TO TRAVERSE ALL IN CURRENT LEVEL
            level_nodes = len(queue)
            first, last = 0, 0

            for i in range(level_nodes):
                #POP FROM QUEUE
                current, index = queue.pop(0)

                print(f"CURRENT = {current.val} INDEX = {index}")

                #CHECK IF FIRST OR LAST
                if i == 0:
                    first = index
                if i == level_nodes - 1:
                    last = index
                
                #ADD LEFT AND RIGHT NODES
                if current.left:
                    queue.append((current.left, 2*index))
                if current.right:
                    queue.append((current.right, (2*index) + 1))
            
            #UPDATE THE MAX WIDTH
            max_width = max(max_width, last - first + 1)

        return max_width

