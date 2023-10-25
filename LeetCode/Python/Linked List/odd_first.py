class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorder_linked_list(head: ListNode) -> ListNode:
    if(head is None):
        return head
    #TWO POINTER APPROACH
    odd_head = head
    even_head = head.next
    
    odd_current = odd_head
    even_current = even_head
    
    while even_current and even_current.next:
        odd_current.next = even_current.next
        odd_current = odd_current.next
        even_current.next = odd_current.next
        even_current = even_current.next
    
    #CONNECT THE TWO LISTS
    odd_current.next = even_head
    return odd_head
    
