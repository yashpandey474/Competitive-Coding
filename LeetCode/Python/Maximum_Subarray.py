# cook your dish here
t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
        
    mx = 0
    curmax = 0
    curmax_back = 0
    for i in range(n):
        
        curmax += a[i]
        curmax_back += a[-i - 1]
        
        if curmax > mx:
            mx = curmax
        if curmax < 0:
            curmax = 0
            
        if curmax_back < 0:
            curmax_back = 0
    
    pos_sum = sum([i for i in b if i > 0])
        
    print(max(pos_sum, pos_sum + curmax, pos_sum + curmax_back, mx))
    