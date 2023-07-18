# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def recursion(self, head, k):
        if head is None:
            return head

        n = 1
        current = head
        while current.next is not None:
            current = current.next
            n+=1

        if n<k:
            return head

        count = 0
        previous = None
        next = None
        current = head

        while current is not None and count < k:
            next = current.next
            current.next = previous 
            previous = current
            current = next
            count += 1

        head.next = self.recursion(current, k)
        return previous
            

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        return self.recursion(head, k)
        
        

