t = int(input())

# ALWAYS BETTER TO INCREASE THE SMALLER NUMBER
def recurse(a, b, n):
    if a > n or b > n:
        return 0
    
    if a < b:
        return 1 + recurse(a + b, b, n)
    
    else:
        return 1 + recurse(a, b + a, n)
    
for test in range(t):
    a, b, n = map(int, input().split())

    print(recurse(a, b, n))
