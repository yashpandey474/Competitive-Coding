class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def split(head):
    #TWO POINTER APPROACH
    slow = head
    front = head.next
    
    while front.next is not None:
        front = front.next
        if front.next:
            front = front.next
            slow = slow.next
            
    #SLOW IS AT MIDDLE NODE
    second = slow.next
    first = head
    slow.next = None
    return first, second

def merge(head1, head2):
    if not head1:
        return head2
        
    if not head2:
        return head1
        
    if head1.val >= head2.val:
        current = ListNode(val = head1.val)
        current.next = merge(head1.next, head2)
        
    elif head1.val < head2.val:
        current = ListNode(val = head2.val)
        current.next = merge(head1, head2.next)
        
    return current
def merge_sort(head):
    #IF NO OR ONE ELEMENT LEFT
    if head is None or head.next is None:
        return head
        
    #SPLIT INTO TWO HALVES
    first, second = split(head)
    
    #RECURSIVELY SPLIT
    first = merge_sort(first)
    second = merge_sort(second)
    
    #MERGE THE LINKED LISTS
    head = merge(first, second)
    
    return head
    
def sort_employee_performance(head: ListNode) -> ListNode:
    #APPLY RECURSIVE MERGE SORT ON LINKEDLIST
    
    head = merge_sort(head)
    return head
