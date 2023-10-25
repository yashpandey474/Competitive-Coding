import math
n = int(input())

def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if (num % i) == 0:
            return False

    return True


arr = ["2"]*(n)

for index in range(n):
    if is_prime(index + 2):
        arr[index] = "1"

if(n>2):print(2)
else: print(1)
print(" ".join(arr))