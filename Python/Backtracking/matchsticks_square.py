class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        #REQUIRED LENGTH
        length_square = sum(matchsticks)//4
        #STORE THE LENGTH OF SIDES
        sides = [0]*4

        if sum(matchsticks)/4 != length_square:
            return False

        matchsticks = sorted(matchsticks, reverse = True)

        def backtrack(index):
            if index >= len(matchsticks):
                return True

            #TRY ADDING THE MATCHSTICK TO EACH OF THE SIDES
            for j in range(4):
                if sides[j] + matchsticks[index] <= length_square:
                    #TRY ADDING TO THIS SIDE
                    sides[j] += matchsticks[index]
                    #CHECK IF IT WORKS
                    if backtrack(index + 1):
                        return True
                    
                    #IF DIDN'T WORK; BACKTRACK
                    sides[j] -= matchsticks[index]

            return False
        return backtrack(0)

