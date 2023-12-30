t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    roads = []
    for j in range(m):
        u, v, w = map(int, input().split())
        roads.append([u, v, w])
        
    bikes = list(map(int, input().split()))
    