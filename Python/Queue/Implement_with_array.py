from typing import List

class Queue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.arr= [0] * 100001
    
    #  Enqueue (add) element 'e' at the end of the queue.
    def enqueue(self, e: int) -> None:
        # Write your code here.
        if self.rear - self.front == 100000:
            return
        self.arr[self.rear] = e
        self.rear += 1
        self.rear = self.rear % 100000

    #  Dequeue (retrieve) the element from the front of the queue.
    def dequeue(self) -> int:
        # Write your code here.
        if self.front == self.rear:
            return -1

        num = self.arr[self.front]
        self.front+=1
        return num
