t = int(input())

def divisible(a):
    return a%3 == 0

for i in range(t):
    n = int(input())
    
    if n == 6 or divisible(n + 1) or divisible(n - 1):
        print("First")
    
    else:
        print("Second")
    