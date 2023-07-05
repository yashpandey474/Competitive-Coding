class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_linked_lists(l1: ListNode, l2: ListNode) -> ListNode:
    # CODE GOES HERE!
    carry = 0
    current = ListNode()
    track = current

    while(l1 is not None or l2 is not None or carry!=0):
        val = carry
        if(l1 is not None):
            val += l1.val
            l1 = l1.next
        if(l2 is not None):
            val += l2.val
            l2 = l2.next

        carry = val//10
        val = val%10
        current.next = ListNode(val=val)
        current = current.next
    
    return track.next
    
