# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def recursion(self, head):
        if not head or not head.next:
            return head

        count = 2
        current = head
        next_node = None
        previous = None
        while count > 0:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
            count -= 1
        
        head.next = self.recursion(current)
        return previous
            


    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None or head.next is None:
            return head
        
        return self.recursion(head)
        
