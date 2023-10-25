t = int(input())



for i in range(t):
    n, k = map(int, input().split())
    
    string = list(input())
    
    
    l = 0
    r = 0
    
    total = 0
    
    while r < k - 1:
        if string[r] == "B":
            total += 1
            
        r += 1
    moves = 0
    
    while r < n:
        if string[l] == "B":
            string[l: r + 1] = ["W" for i in range(l, r + 1)]
            total = 0
            moves += 1
        
        if string[r] == "B":
            total += 1
            
        if r == n - 1 and total != 0:
            moves += 1
            total = 0
        
        l += 1
        r += 1
    
    print(moves)
        