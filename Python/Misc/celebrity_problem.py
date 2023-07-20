def findCelebrity(n, knows):

    # Write your code here.    

    #FIRST PASS
    c = 0
    for i in range(1, n):
        if knows(c, i):
            c = i

    #SECOND PASS
    for i in range(n):
        if (i != c) and ((knows(c, i)) or (not knows(i, c))):
            return -1

    return c
    pass
