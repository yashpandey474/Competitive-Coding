#USE A DLL
class Node:
    def __init__(self, val = "", next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class DLL:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def addNode(self, node):
        self.head.next.prev = node
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head

class BrowserHistory:

    def __init__(self, homepage: str):
        self.root = DLL()
        self.root.addNode(Node(val = homepage))
        self.current = self.root.head.next

    def visit(self, url: str) -> None:
        newNode = Node(val = url)
        self.current.next = newNode
        newNode.prev = self.current
        newNode.next = self.root.tail
        self.root.tail.prev = newNode

        self.current = newNode
        

    def back(self, steps: int) -> str:
        while self.current.prev != self.root.head and steps > 0:
            self.current = self.current.prev
            steps -= 1

        return self.current.val
        

    def forward(self, steps: int) -> str:
        while self.current.next != self.root.tail and steps > 0:
            self.current = self.current.next
            steps-=1

        return self.current.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
