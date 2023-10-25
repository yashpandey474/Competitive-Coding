from math import gcd
t = int(input())

for i in range(t):
    l, r = map(int, input().split())
    
    
    #NO ANSWER EXISTS
    if r <= 3:
        print(-1)
        continue
    
    #UNEQUAL LEFT AND RIGHT
    if l != r:
        print(r//2, r//2)
        continue
    
    #EQUAL LEFT AND RIGHT
    remainder, flag = 2, 0
    
    while remainder % remainder <= l:
        if l % remainder == 0 and l/remainder != 0 and l*(remainder - 1)/remainder != 0 and l/remainder != 1:
            flag = 1
            break
        remainder += 1
        
    if flag:
        print(l//remainder, l*(remainder - 1)//remainder)
        continue
    else:
        print(-1)
        continue
    
            
    

    
        
    