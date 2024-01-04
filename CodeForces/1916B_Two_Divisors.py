import math
t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    
    # A IS A DIVISOR OF B
    if b % a == 0:
        # B = A.P WHEE P IS THE SMALLEST PRIME FACTOR OF X
        print(b*b//a)
        
    else:
        # b = x / p and a = x / q and p, q aer he two smallest prime factors of x
        print(b*a//math.gcd(a, b))
    