def isCyclicRotation(p: str, q: str) -> int:
    # Write your code here.
    n = len(p)

    def equal(str1, str2, start1):
        i = start1
        j = 0

        for m in range(n):
            if str1[(i + m)%n] != str2[m]:
                return False
        
        return True

    for i in range(n):
        if equal(p, q, i):
            return 1


    return 0
