t = int(input())

for i in range(t):
    n = int(input())
    s = str(input())
    
    flag = False
    count_0s = 0
    count_1s = 0
    
    for j in range(len(s)):
        if j < len(s) - 1:
            if int(s[j]) ^ int(s[j + 1]) == 1:
                flag = True
                
        if s[j] == "0":
            count_0s += 1
            
        else:
            count_1s += 1
            
    if count_1s < count_0s or flag:
        print("YES")
        
    else:
        print("NO")
        
        