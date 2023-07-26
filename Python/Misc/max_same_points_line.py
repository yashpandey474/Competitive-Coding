class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        #STORE MAX NUMBER OF POINTS
        max_points = 0

        #ITERATE FOR EACH POINT
        
        for i in range(len(points)):
            same = 0
            map_points = defaultdict(int)
            #FOR EVERY OTHER POINT
            for j in range(i + 1, len(points)):
                #IF SAME POINTS
                if points[j][0] == points[i][0] and points[j][1] == points[i][1]:
                    same+=1

                #IF INFINITE SLOP
                elif points[j][0] == points[i][0]:
                    map_points[float('inf')]+=1

                #OTHER SLOPE
                else:
                    slope = (points[i][1] - points[j][1])/(points[i][0] - points[j][0])
                    map_points[slope]+=1
            print(map_points)
            max_here = max(map_points.values(), default = 0) 
            max_here += same

            max_points = max(max_points, max_here)

        return max_points+1


