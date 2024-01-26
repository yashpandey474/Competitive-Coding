t = int(input())
import math
for i in range(t):
    # ORDER & NUMBER OF CHAINS
    n, m = map(int, input().split())
    
    # SIZES OF EACH CHAIN
    a = list(map(int, input().split()))
    
    if m == 1:
        print(0)
        continue
    
    # CHOOSE THE LINKING DONUTS FROM SMALLEST CHAIN
    
    # SORT THE LENGTHS OF CHAINS
    a = sorted(a)
    
    # REQ NUMBER OF LINKS
    req_links = m - 1
    count = 0
    
    for j in range(m):
        # REMAINING PIECES
        rem = m - (j + 1)
        count += a[j]
        
        # CAN CONNECT REMAINING WITH SO FAR
        if count >= rem - 1:
            # ALL CHAINS SO FAR DESTROYED
            if count == rem - 1:
                print(rem - 1)
                break
                
            # NEED ONE MORE TO LINK REM FROM CURRENT CHAIN
            else:
                print(rem)
                break
                
            
    
    