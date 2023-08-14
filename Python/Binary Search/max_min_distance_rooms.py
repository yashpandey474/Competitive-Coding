from os import *
from sys import *
from collections import *
from math import *

def chessTournament(positions, n , c):

    #MAXIMISE THE MINIMUM DISTANCE BETWEEN POSITIONS
    positions = sorted(positions)

    #FIND IF POSSIBLE TO ASSIGN ROOMS
    def canAssign(max_min_distance):
        assigned = 1
        prev = positions[0]

        for i in range(1, n):
            if positions[i] - prev >= max_min_distance:
                assigned += 1
                prev  = positions[i]

        return assigned >= c
            
    #LEAST POSSIBLE
    left = 1
    #MAXIMUM POSSIBLE
    right = max(positions)

    #BINARY SEARCH
    while left <= right:
        #CALCULATE MID
        mid = (left + (right - left)//2)

        #SEE IF VALID VALUE
        if canAssign(mid):
            #UPDATE 
            left = mid + 1

        else:
            right = mid - 1

    return right

