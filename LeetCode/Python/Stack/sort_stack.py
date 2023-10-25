from os import *
from sys import *
from collections import *
from math import *


def sortedInsert(stack, num):
    if len(stack) == 0 or stack[-1] < num:
        stack.append(num)
    else:
        top = stack.pop()
        sortedInsert(stack, num)
        stack.append(top)
def sortStack(stack):
    # given data structure is a python list 
    # as list have all the similar operations available so use them
    # Write your code here
    

    if len(stack) > 0:
        num = stack.pop()
        sortStack(stack)
        sortedInsert(stack, num)

    return stack
