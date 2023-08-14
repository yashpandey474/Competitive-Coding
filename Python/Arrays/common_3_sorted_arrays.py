from os import *
from sys import *
from collections import *
from math import *

def findCommonElements(a,b,c):
    i = 0
    j = 0

    n1 = len(a)
    n2 = len(b)
    n3 = len(c)
    result = set()

    def binSearchC(ele):
        st = 0
        en = n3 - 1

        while st <= en:
            mid = st + (en - st)//2

            if c[mid] == ele:
                return True

            elif c[mid] > ele:
                en = mid - 1

            else:
                st = mid + 1

        return False

    #FIND COMMON ELEMENTS IN FIRST TWO ARRAYS
    while i < n1 and j < n2:
        if a[i] < b[j]:
            i += 1

        elif a[i] > b[j]:
            j += 1

        else:
            if binSearchC(a[i]):
                result.add(a[i])
            i += 1
            j += 1

    return list(result)
