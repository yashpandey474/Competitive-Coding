t = int(input())

for test in range(t):
    n = int(input())
    s = str(input())
    a1 = 0
    a2 = -1
    
    for i in range(n):
        if s[i] == "B":
            a1 = i
            break
        
    for  i in range(n - 1, -1, -1):
        if s[i] == "B":
            a2 = i
            break
        
    print(a2 - a1 + 1)