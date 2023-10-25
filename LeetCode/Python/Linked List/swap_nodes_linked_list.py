# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #GET TO MIDDLE OF LINKED LIST
        if not head or not head.next:
            return head
        count = 0
        slow = head
        fast = head

        while fast and count < k:
            fast = fast.next
            count += 1


        if not fast:
            #LAST AND FIRST NODE
            kthEnd = head
            curr = head
            while curr.next:
                curr = curr.next
            kthBeg = curr

            kthBeg.val, kthEnd.val = kthEnd.val, kthBeg.val
            return head


        while fast and fast.next:
            fast = fast.next
            slow = slow.next


        kthEnd = slow.next

        count = 1
        slow = head
        while slow and count < k:
            slow = slow.next
            count += 1

        kthBeg = slow

        kthBeg.val, kthEnd.val = kthEnd.val, kthBeg.val
        return head

        
