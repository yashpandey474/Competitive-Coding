t = int(input())
import math
for i in range(t):
    n, p, k = map(int, input().split())
    
    ans = 0
    
    # REMAINDER
    rem = p%k
    
    # MAX MULTIPLE OF K IN range
    last = (n // k)*k
    
    complete_sequences = last//k
    
    # NUMBERS WITH LESS REMAINDER THAN P
    ans += (p%k)*(complete_sequences)
    
    # SAME MODULE BUT BEFORE    
    ans += p // k
    
    # NUMBERS AFTER LAST WITH LOWER MODULO K THAN P
    ans += min(p%k, n%k)
    
    print(ans + 1)