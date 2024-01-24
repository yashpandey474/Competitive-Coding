import sys

def get_int():
    return int(sys.stdin.readline().strip())


t = get_int()

for i in range(t):
    n = get_int()
    x = (n - 1)*(n - 2)
    print(x + 1)