# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head1):
        if head1 is None or head1.next is None:
            return head1

        next_node = None
        prev_node = None
        current = head1

        while current:
            next_node = current.next
            current.next = prev_node
            prev_node = current
            current = next_node

        return prev_node
        




    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        #REVERSE THE LISTS
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)

        current = ListNode()
        tracker = current
        carry = 0

        while l1 or l2:
            node_val = carry

            if l1:
                node_val += l1.val
                l1 = l1.next

            if l2:
                node_val += l2.val
                l2 = l2.next
            carry = node_val//10
            node_val = node_val%10
            tracker.next = ListNode(val = node_val)
            tracker = tracker.next

        if carry:
            tracker.next = ListNode(val = carry)

        return self.reverse(current.next)
