class Solution:
    #Function to convert a binary tree into its mirror tree.
    def isLeaf(self, root):
        if not root.right and not root.left:
            return True
            
        return False
        
    def recursion(self, root):
        #BASE CASE
        if root is None or self.isLeaf(root):
            return root
            
        
        #EXCHANGE ROOT
        temp = root.left
        root.left = self.mirror(root.right)
        root.right = self.mirror(root.left)
        
        return root
            
            
    def mirror(self,root):
        # Code here
        
        #BASE CASE
        if root is None or self.isLeaf(root):
            return
        
        #EXCHANGE
        return self.recursion(root)
        
