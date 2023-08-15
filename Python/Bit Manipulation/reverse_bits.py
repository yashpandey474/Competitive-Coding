def reverseBits(n):
    # Write your code here.
    rev = ""
    while n:
        rev = rev +  str(n & 1)
        n >>= 1

    res = 0
    if len(rev) < 32:
        rev += "0"*(32 - len(rev))

    # print("REV = ", rev)

    for i in range(len(rev)-1, -1, -1):
        res += (pow(2, (len(rev) - 1 - i))) * int(rev[i])

    return res
