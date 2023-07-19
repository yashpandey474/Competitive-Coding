class Node:
    def __init__(self, val = None, next = None, prev = None, key = None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

class DLL:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    #O(1) OPERATION
    def insertNode(self, key, value):
        newNode = Node(val = value, key = key)
        self.head.next.prev = newNode
        newNode.next = self.head.next
        newNode.prev = self.head
        self.head.next = newNode

        return newNode

    #O(1) OPERATION
    def removeLast(self):
        if self.tail.prev == self.head:
            return
        
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


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
            #PASS THE NODE TO REMOVE
            self.DLL.removeNode(self.map[key])
            self.map[key] = self.DLL.insertNode(key = key, value = self.map[key].val)
            return self.map[key].val
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.map:
            #PASS NODE TO REMOVE
            self.DLL.removeNode(self.map[key])
            node = self.DLL.insertNode(key = key, value = value)
            self.map[key] = node

        #DONT HAVE TO REMOVE
        elif len(self.map) < self.capacity:
            node = self.DLL.insertNode(key = key, value = value)
            self.map[key] = node

        #HAVE TO REMOVE
        else:
            key_delete = self.DLL.tail.prev.key
            del self.map[key_delete]
            self.DLL.removeLast()
            node = self.DLL.insertNode(key = key, value = value)
            self.map[key] = node
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
