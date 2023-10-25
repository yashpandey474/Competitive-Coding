# cook your dish here

def isSubseq(string, subseq):
    i = 0
    j = 0
    
    while i < len(string) and j < len(subseq):
        if string[i] == subseq[j]:
            j += 1
        i += 1
        
    return j == len(subseq)
    
t = int(input())
for i in range(t):
    m, w = input().split()


    #IF EQUAL LENGTH
    if isSubseq(m, w) or isSubseq(w, m):
        print("YES")
    else:
        print("NO")
            
    
        
