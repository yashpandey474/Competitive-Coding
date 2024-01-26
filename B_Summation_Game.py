t = int(input())

for i in range(t):
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))

    total = sum(a)
    a = sorted(a, reverse = True)
    
    # PREFIX SUM ARRAY
    prefix_sum = [a[i] for i in range(n)]
    
    for i in range(1, n):
        prefix_sum[i] += prefix_sum[i - 1]
        
    print("PREFIX SUM", prefix_sum)
    
    curr_diff = -float('inf')
    
    # COUNT -> NUMBER OF ELEMENTS TO REMOVE
    for count in range(1, k + 1):
        
        # ONLY ONE ELEMENT IN ARRAY
        if count == (n):
            curr_diff = 0
            break
        
        # CURRENT MAXIMUM ELEMENTS
        max_ele = prefix_sum[count - 1]
        
        # ELEMENTS THAT BOB CAN REMOVE
        next_max = prefix_sum[count + x - 1] - max_ele
        
        # DIFFERENCE IF NEXT MAXIMUM ELEMENT IS REMOVED
        next_diff = total - max_ele - 2*next_max
        
        print("COUNT %d MAX_ELE %d NEXT_MAX %d CURR_DIFF %d NEXT_DIFF %d\n" % (count, max_ele, next_max, curr_diff, next_diff))

        curr_diff = max(curr_diff, next_diff)
        
        count += 1
        
    print(curr_diff)
        