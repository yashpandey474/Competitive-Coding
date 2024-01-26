t = int(input())

for i in range(t):
    n, w1, wt = map(int, input().split())
    w = list(map(int, input().split()))
    
    if w1 <= wt:
        print("YES")
        continue
    
    curr_weight = wt
    curr_set = set()
    
    for weight in w:
        
        if weight in curr_set:
            curr_weight += 2*weight
            curr_set.remove(weight)
            
        else:
            curr_set.add(weight)

    # print("CURR_WEIGHT", curr_weight)
    if curr_weight >= w1:
        print("YES")
        continue
    
    print("NO")
    
    