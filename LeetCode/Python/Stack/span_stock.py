from typing import List

def findStockSpans(prices: List[int]) -> List[int]:
    # Write your code here.
    n = len(prices)
    span = [1]*n
    stack = []

    for i in range(n):
        
        while stack and prices[stack[-1]] < prices[i]:
            stack.pop()

        if stack:
            span[i] = i - stack[-1]
        
        elif not stack:
            span[i] = i+1

        stack.append(i)

    return span
