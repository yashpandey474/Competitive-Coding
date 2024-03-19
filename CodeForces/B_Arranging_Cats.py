t = int(input())
for i in range(t):
    n = int(input())
    s = str(input())
    f = str(input())
    
    s1 = 0
    f1 = 0
    c1 = 0
    
    for j in range(n):
        if s[j] == "1":
            s1 += 1
        
        if f[j] == "1":
            f1 += 1
            if s[j] == "1":
                c1 += 1
    
    # print("F1, s1, c1", f1, s1, c1) 
    x = abs(s1 - c1)
    y = abs(f1 - c1)
    z = abs(f1 - s1)
    
    print((x + y + z)//2)   
        