# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return head

        if head.next is None:
            return None

        slow = head
        previous = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            previous = slow
            slow = slow.next
            
        if slow is None:
            return head

        previous.next = slow.next
        return head
