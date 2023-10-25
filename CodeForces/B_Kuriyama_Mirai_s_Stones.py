n = int(input())

costs = list(map(int, input().split()))

quest = int(input())


arrange = sorted(costs)
prefix = [0]*n

prefix[0] = costs[0]

prefix_arr = [0]*n

prefix_arr[0] = arrange[0]

for i in range(1, n):
    prefix[i] = costs[i] + prefix[i - 1]
    
for i in range(1, n):
    prefix_arr[i] = arrange[i] + prefix_arr[i - 1]


for i in range(quest):
    ty, l, r = map(int, input().split())
    
    
    if ty == 1:
        print(prefix[r - 1] - prefix[l - 1] + costs[l - 1])
        
    else:
        print(prefix_arr[r - 1] - prefix_arr[l - 1] + arrange[l - 1])