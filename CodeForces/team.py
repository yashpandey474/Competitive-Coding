n = int(input())

total = 0
for i in range(n):
    curr = sum(list(map(int, input().split())))
    if curr >= 2:
        total += 1
        
print(total)