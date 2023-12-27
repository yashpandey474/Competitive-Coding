t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    if k == 1:
        if a != sorted(a):
            print("NO")
        else:
            print("YES")
            
    else:
        print("YES")
    
    