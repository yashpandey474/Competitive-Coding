def towerOfHanoi(n):
    # Write your code here
    # Return a 2-D array
    

    m = []


    def moveDisk(disks, toRod,  fromRod, moves):
        #MOVES IS A 2D ARRAY FOR THE MOVES
        if disks == 1:
            moves.append([fromRod, toRod])
            return
        
        #NUMBER OF THE THIRD ROD
        i = 1 ^ 2 ^ 3 ^ toRod ^ fromRod
            
        #RECURSIVELY MOVE FROM TO REMO
        moveDisk(disks - 1, i, fromRod, moves)

        #MOVE HEAVIEST DISK TO TOROD
        moves.append([fromRod, toRod])

        #MOVE N-1 DISKS FROM REM TO TOROD
        moveDisk(disks - 1, toRod, i, moves)

    moveDisk(n, 2, 1, m)
    return m
    

