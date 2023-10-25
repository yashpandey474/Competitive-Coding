t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    
    arr = list(map(int, input().split()))
    
    if k not in arr:
        print("NO")
        continue
    
    print("YES")