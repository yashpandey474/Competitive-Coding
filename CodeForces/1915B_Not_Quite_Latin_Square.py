t = int(input())

for i in range(t):
    square = []
    
    for j in range(3):
        row = list(str(input()))
        square.append(row)
        
    total = ord("A") + ord("B") + ord("C")
    
    # find row and column of "?"
    row, col = -1, -1
    for r in range(3):
        for c in range(3):
            if square[r][c] == "?":
                row, col = r, c
                break
             
    # find sum in row
    curr_sum = 0
    for c in range(3):
        if c != col:
            curr_sum += ord(square[row][c])
            
    print(chr(total - curr_sum))
                