"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        #HASHMAP TO STORE COPIES
        map_copies = {}
        
        if head is None:
            return None
        
        temp = head
        while temp != None:
            newNode = Node(x = temp.val)
            map_copies[temp] = newNode
            temp = temp.next

        temp = head
        copyHead = map_copies[temp]
        copyTracker = copyHead
        while temp != None:
            copyTracker = map_copies[temp]
            if temp.next != None:
                copyTracker.next = map_copies[temp.next]
            if temp.random != None:
                copyTracker.random = map_copies[temp.random]
            temp = temp.next
            copyTracker = copyTracker.next

        return copyHead
