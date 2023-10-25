class Solution:


    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:

        #THE DISTANCES BETWEEN ALL POINTS SHOUDL EITHER BE THE SIDE LENGTH OR THE DIAGONAL LENGTH [2 UNIQUE VALUES]

        distances = set()
        
        def distance(p1, p2):
            return (p1[0] - p2[0])**2 + (p1[1]-p2[1])**2

        #ADD DISTANCES BETWEEN ALL PAIRS
        distances.add(distance(p1, p2))
        distances.add(distance(p1, p3))
        distances.add(distance(p1, p4))
        distances.add(distance(p3, p2))
        distances.add(distance(p4, p2))
        distances.add(distance(p3, p4))

        #CHECK NO ZERO [SAME POINT]
        if 0 in distances:
            return False

        return len(distances) == 2

        
