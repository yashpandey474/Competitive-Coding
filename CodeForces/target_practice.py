t = int(input())

for i in range(t):
    total = 0
    grid = []
    
    for i in range(10):
        row = list(input())
        
        for col, ele in enumerate(row):
            if ele == "X":
                if i == 0 or i == 9 or col == 0 or col == 9:
                    total += 1
                
                elif i == 1 or i == 8 or col == 1 or col == 8:
                    total += 2
                    
                elif i == 2 or i == 7 or col == 2 or col == 7:
                    total += 3
                    
                elif i == 3 or i == 6 or col == 3 or col == 6:
                    total += 4
                    
                elif i == 4 or i == 5 or col == 4 or col == 5:
                    total += 5
                    
    print(total)
        
        
    