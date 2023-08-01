# List Node Class.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def mergeSort(head):
    def splitLinkedLists(head):
        if head is None or head.next is None:
            return head, None

        #FIND MIDDLE NODE
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        right = slow.next
        slow.next = None

        return head, right

    def merge(head1, head2):
        if not head1:
            return head2

        if not head2:
            return head1
        result = None
        if head1.data <= head2.data:
            result = Node(head1.data)
            result.next = merge(head1.next, head2)

        else:
            result = Node(head2.data)
            result.next = merge(head1, head2.next)

        return result 
    # Write your code here.
    if not head or not head.next:
        return head
    
    left, right = splitLinkedLists(head)
    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)



	

def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

def printll(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

# Main.
# Read the link list elements including -1.
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list.
l = ll(arr[:-1])
l = mergeSort(l)
printll(l)
