t = int(input())

for i in range(t):
    n = int(input())
    digits = list(map(int, input().split()))
    
    digits = sorted(digits)
    digits[0] = digits[0] + 1
    i = 1
    
    for a in digits:
        i *= a
        
    print(i)