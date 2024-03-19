t = int(input())
for i in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    if n <= 2:
        print(0)
        continue
    
    # CANNOT FORM TRIANGLE: A + B > C for the sides
    # nums = list(set(nums))
    def canTriangle(a, b, c):
        if a == 0 or b == 0 or c == 0:
            return False
        
        if a + b <= c or a + c <= b or b + c <= a:
            return False
        
        return True
    
    n = len(nums)
    count = 0
    for a in range(n):
        for b in range(a + 1, n):
            for c in range(b + 1, n):
                print(nums[a], nums[b], nums[c], canTriangle(nums[a], nums[b], nums[c]))
                if canTriangle(nums[a], nums[b], nums[c]):
                    count+=1
                    
    print(count)
    