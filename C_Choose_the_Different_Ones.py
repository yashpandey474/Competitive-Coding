for test in range(int(input())):
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    map1 = set()
    map2 = set()
    map3 = set()
    count1 = 0
    
    for ele in a:
        if 1 <= ele <= k:
            map1.add(ele)
            
    for ele in b:
        if 1<=ele<=k and ele not in map1:
            map2.add(ele)
            
        if ele in map1:
            map3.add(ele)
            
    map1 = set()
    for ele in a:
        if 1<=ele<=k and ele not in map3:
            map1.add(ele)
            
    unique1 = len(map1)
    unique2 = len(map2)
    common = len(map3)
            
    # print(map1, map2, map3)
    if unique1 <= k/2 and unique2 <= k/2 and (unique1 + unique2 + common) == k:
        print("YES") 
        
    else:
        print("NO")
    
            
        
    
    