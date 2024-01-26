t = int(input())
import math
        
    
for i in range(t):
    n = int(input())
    s = str(input())
    
    first_occur = [-1 for j in range(26)]
    total_count = 0
    
    for j in range(n):
        if first_occur[ord(s[j]) - ord('a')] < 0:
            first_occur[ord(s[j]) - ord('a')] = j
            number_second_ops = (n - j)
            total_count += number_second_ops
            
    print(total_count)
    