# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head):
        if head is None or head.next is None:
            return head

        next_node = None
        previous = None
        current = head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        #L0 -> L1 -> .... -> LN TO L0 -> LN -> L1 -> LN-1
        #FIND MIDDLE OF LISTx
        slow = head
        fast = head
        if not head:
            return head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        #REVERSE HALF AFTER MIDDLE
        slow.next = self.reverse(slow.next)

        #ADD NODES FROM AFTER THE MIDDLE
        track1 = head
        track2 = slow.next
        #UNTIL NODE ALREADY CONNECTED TO OTHER HALF
        while track1 != slow:
            slow.next = track2.next
            track2.next = track1.next
            track1.next = track2
            track1 = track2.next
            track2 = slow.next
