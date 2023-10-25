# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        #SERIALIZE: CREATE A STRING FROM THE ROOT OF BINARY TREE
        #PERFORM A LEVEL ORDER TRAVERSAL
        queue = []
        result = ""
        if not root:
            return result
        queue.append(root)

        while queue:
            current = queue.pop(0)
            
            if current is not None:
                result += str(current.val) + ","
                queue.append(current.left)
                queue.append(current.right)
            
            else:
                result += "#,"
        return result.rstrip(",")
    
    def getNext(self, string, index):
        number = 0
        sign = 1

        if index >= len(string) or string[index] == "#":
            return None, index+2

        while index < len(string) and string[index] != ',':
            if string[index] == "-":
                sign = -1
                index+=1
            number = number*10 + int(string[index])
            index += 1

        return number*sign, index+1

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        print("DATA  = ", data)

        #RETURN THE ROOT OF BINARY TREE CONSTRUCTED FROM STRING
        if data == "":
            return None
        
        number, index = self.getNext(data, 0)

        newRoot = TreeNode(number)
        queue = [newRoot]

        while queue and index<len(data):
            current = queue.pop(0)
            leftNumber, index = self.getNext(data, index)
            rightNumber, index = self.getNext(data, index)
            
            print("CURRENT = ", current.val, "LEFT = ", leftNumber, "RIGHT = ", rightNumber)
            #CREATE NODES IF NOT NODE
            if leftNumber is not None:
                current.left = TreeNode(leftNumber)
                queue.append(current.left)
            
            if rightNumber is not None:
                current.right = TreeNode(rightNumber)
                queue.append(current.right)

        return newRoot


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
