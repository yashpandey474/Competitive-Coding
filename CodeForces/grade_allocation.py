t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    
    
    print(min(m, sum(arr[1: ]) + arr[0]))
               
    