class Node:
    def __init__(self, val = None, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class DLL:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def insertNode(self, key):
        newNode = Node(val = key)
        self.head.next.prev = newNode
        newNode.next = self.head.next
        newNode.prev = self.head
        self.head.next = newNode

    def removeLast(self):
        if self.tail.prev == self.head:
            return
        
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev

    def removeNode(self, key):
        current = self.head.next
        previous = self.head

        while current is not None and current.val != key:
            previous = current
            current = current.next
        
        if current is not None:
            previous.next = current.next
            if current.next is not None:
                current.next.prev = previous
        


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.DLL = DLL()
        self.map = {}
        self.capacity = capacity
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """

        #IN HASHMAP
        if key in self.map:
            self.DLL.removeNode(key)
            self.DLL.insertNode(key)
            return self.map[key]
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.map:
            self.DLL.removeNode(key)
            self.map[key] = value
            self.DLL.insertNode(key)

        #DONT HAVE TO REMOVE
        elif len(self.map) < self.capacity:
            self.map[key] = value
            self.DLL.insertNode(key)

        #HAVE TO REMOVE
        else:
            key_delete = self.DLL.tail.prev.val
            del self.map[key_delete]
            self.DLL.removeLast()
            self.map[key] = value
            self.DLL.insertNode(key)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
