import queue
import sys
sys.setrecursionlimit(10**6)

class BinaryTreeNode:
    
    def __init__(self, data):
        
        self.data = data
        self.left = None
        self.right = None


def countUnivalTrees(root):
    
    # Write your code here.
    # This function returns the updated root.
    
    count = 0
    def dfs(node):
        nonlocal count

        if not node:
            return True, None

        left_unival, left_val = dfs(node.left)
        right_unival, right_val = dfs(node.right)

        if left_unival and right_unival and ((left_val is None or left_val == node.data) and (right_val is None or right_val == node.data)):
            count += 1
            return True, node.data

        else:
            return False, None

        

    dfs(root)
    return count

        



def buildLevelTree(levelorder):
    
    index = 0
    length = len(levelorder)
    
    if length<=0 or levelorder[0]==-1:
        return None
    
    
    root = BinaryTreeNode(levelorder[index])
    index += 1
    
    q = queue.Queue()
    q.put(root)
    
    while not q.empty():
        
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        
        if leftChild != -1:
            
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
            
        rightChild = levelorder[index]
        index += 1
        
        
        if rightChild != -1:
            
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
            
            
    return root
    
t = int(input())
while t >0:
    li = [int(i) for i in input().split()]
    root = buildLevelTree(li)
    print(countUnivalTrees(root))
    t = t -1


            
            

