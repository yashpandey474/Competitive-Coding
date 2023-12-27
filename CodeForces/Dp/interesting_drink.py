shops = int(input())
prices = sorted(list(map(int, input().split())))
days  = int(input())


for i in range(days):
    coins = int(input())
    
    #APPLY BINARY SEARCH
    left = 0
    right = shops - 1
    found = False
    
    while left <= right:
        mid = left + (right - left)//2
        
        if mid == 0:
            if prices[mid] > coins:
                print(0)
                found = True
                break
            
        if prices[mid] > coins:
            if prices[mid - 1] <= coins:
                print(mid)
                found = True
                break    
            right = mid - 1
            
        if prices[mid] <= coins:
            if mid == shops - 1:
                print(shops)
                found = True
                break
            
            if prices[mid + 1] > coins:
                print(mid + 1)
                found = True
                break
            
            left = mid + 1
            
    if not found:
        print(left)
    
