def getMinimumAnagramDifference(str1, str2):
    # Write your code here.
    str1 = sorted(str1)
    str2 = sorted(str2)
    
    n = len(str1)
    result = n

    i = 0
    j = 0
    while i < n and j < n:
        if str1[i] < str2[j]:
            i += 1

        elif str1[i] > str2[j]:
            j += 1

        else:
            result -= 1
            i+=1
            j+=1

    return result
