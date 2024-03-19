t = int(input())
for i in range(t):
    n = int(input())
    a = str(input())
    b = str(input())
    c = str(input())
    
    # A AND B MATCH TEMPLATE AND C DOESNT
    flag = False
    for j in range(n):
        if a[j] != c[j] and b[j] != c[j]:
            print("YES")
            flag = True
            break
        
    if not flag:
        print("NO")
        