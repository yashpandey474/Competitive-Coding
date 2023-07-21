class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1
    
    if list1.val <= list2.val:
        current = ListNode(val = list1.val)
        current.next = merge(list1.next, list2)
        
    else:
        current = ListNode(val = list2.val)
        current.next = merge(list1, list2.next)
    
    return current
def merge_k_lists(lists: list[ListNode]) -> ListNode:
    #MERGE ALL PAIRS OF LINKED LISTS
    if not lists:
        return None
        
    current = lists[0]
    for i in range(1, len(lists)):
        current = merge(current, lists[i])
    
    return current
