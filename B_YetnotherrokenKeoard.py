t = int(input())

for i in range(t):
    s  = list(str(input()))
    set1 = set()
    
    set1.add("B")
    set1.add("$")
    set1.add("b")
    
    lowerIndex = []
    upperIndex = []
    for m in range(len(s)):
        a = s[m]
        
        if a == "b":
            if len(lowerIndex) != 0:
                lI = lowerIndex.pop()        
                s[lI] = "$"
                                                    
        elif a == "B":
            if len(upperIndex) != 0:
                uI = upperIndex.pop()
                s[uI] = "$"
                
        else:
            if a >= "a" and a <= "z":
                lowerIndex.append(m)
            else:
                upperIndex.append(m)
                
    for m in range(len(s)):
        if s[m] in set1:
            continue
 
        print(s[m], end = "")
    
    print()