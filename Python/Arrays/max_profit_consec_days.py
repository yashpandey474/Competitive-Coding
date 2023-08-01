from os import *
from sys import *
from collections import *
from math import *

def maximumProfit(profit, n, a, b):
    # Write your code here
    # Return an integer denoting the answer
    maxProfit = 0
    # currProfit = -float('inf')

    for i in range(n):
        currProfit = 0
        #STARTING POINTS
        for j in range(i, min(i + b, n)):
            currProfit += profit[j]

            #CHECK IF HAS A
            if (j >= (i + a - 1)):
                maxProfit = max(maxProfit, currProfit)
    return maxProfit

