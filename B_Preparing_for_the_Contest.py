t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    
    #PROBLEMS FROM 1 TO N WITH DIFFICULTY FROM 1 TO N
    a = [j + 1 for j in range(n)]
    
    #K TIMES THAT MORE DIFFICULT RIGHT AFTER LESS DIFFICULT
    positions = [n - k - 1]
    for j in range(k):
        positions.append(n - j - 1)
    
    # Generate the order by swapping elements at excitement positions
    print(positions)
    for pos in positions:
        a[pos], a[pos + 1] = a[pos + 1], a[pos]
        
    print(" ".join(map(str, a)))