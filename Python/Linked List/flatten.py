class Node:
    def __init__(self, val=0, next=None, child=None):
        self.data = val
        self.next = next
        self.child = child


# Don't change the code above.


def merge(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    if head1.data <= head2.data:
        new = head1
        new.child = merge(head1.child, head2)
        return new
    else:
        new = head2
        new.child = merge(head1, head2.child)
        return new

def flattenLinkedList(head: Node) -> Node:
    # Write your code here
    if head is None or head.next is None:
        return head

    #MERGE SORTED LINKED LISTS
    head.next = flattenLinkedList(head.next)
    head = merge(head, head.next)
    return head
