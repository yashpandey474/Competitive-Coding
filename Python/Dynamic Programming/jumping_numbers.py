from os import *
from sys import *
from collections import *
from math import *

def jumpingNumbers(n):

    #START WITH SINGLE DIGIT NUMBERS AS SEEDS
    jumping = set()
    for i in range(10):

        #CREATE A QUEUE
        queue = [i]
        
        #ITERATE
        while queue:
            curr = queue.pop(0)

            #ONLY IF IN REQUIRED RANGE
            # print("CURR = ", curr)
            if curr <= n:
                #APPEND TO RESULT
                jumping.add(curr)

                #CHECK LAST DIGIT
                last_digit = curr % 10

                if last_digit == 0:
                    queue.append(curr*10 + 1)

                elif last_digit == 9:
                    queue.append(curr*10 + 8)

                else:
                    queue.append(curr*10 + last_digit + 1)
                    queue.append(curr*10 + last_digit - 1)

    return sorted(list(jumping))
