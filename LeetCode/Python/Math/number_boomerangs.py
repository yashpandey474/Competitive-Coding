class Solution:
    def distance(self, p1, p2):
        return (p1[0]-p2[0])**2 + (p1[1]  - p2[1])**2
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:

        #CREATE A MAP TO STORE DISTANCES
        map_distances = {}

        result = 0
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j:
                    continue
                dist = self.distance(points[i], points[j])

                if dist not in map_distances:
                    map_distances[dist] = 0

                map_distances[dist] += 1
            
             #CALCULATE TRIPLETS

            for i in map_distances.values():
                result += i * (i-1)

            map_distances = {}

        return result



       

        return result

                
                
