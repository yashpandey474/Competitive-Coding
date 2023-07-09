# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def getInorder(self, root):
        stack = []
        result = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.val)
            current = current.right

        return result

    def __init__(self, root: Optional[TreeNode]):
        self.pointer = -1
        self.inorder = self.getInorder(root)

    def next(self) -> int:
        self.pointer += 1
        return self.inorder[self.pointer]

    def hasNext(self) -> bool:
        return self.pointer != len(self.inorder)-1
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
