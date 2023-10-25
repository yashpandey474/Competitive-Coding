import math
n = int(input())

if n == 1:
    print(1)
    print(1)
    quit()
    
def is_prime(num):
    for i in range(math.sqrt(num)):
        if (num % i) == 0:
            return False
        
    return True

arr = [2]*(n)

for index in range(n):
    if is_prime(index + 2):
        arr[index] = 1
        
print(2)
print(" ".join(arr))