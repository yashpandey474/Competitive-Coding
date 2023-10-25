class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        #CALCULATE TIME TAKEN
        time = [dist[i]/speed[i] for i in range(n)]

        #LOWEST TIME TO REACH TO HIGHEST TIME TO REACH
        time = sorted(time)
        #INITIAL TIME IS 0
        current = 0
        eliminated = 0

        print(time)
        for i in range(n):
            if time[i] > current:
                eliminated += 1
                current += 1

            else:
                break

        return eliminated
