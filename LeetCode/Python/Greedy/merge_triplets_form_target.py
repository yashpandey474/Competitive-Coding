class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        #ANY TRIPLET WITH AN ELEMENT GREATER THAN CORRESPONDING ELEMENT OF TARGET; NEVER CONSIDERED
        useful = []
        have = [0]*3
        for i in triplets:
            if i[0] <= target[0] and i[1] <= target[1] and i[2] <= target[2]:
                useful.append(i)

        for i in useful:
            if i[0] == target[0] and have[0] == 0:
                have[0] = 1

            if i[1] == target[1] and have[1] == 0:
                have[1] = 1

            if i[2] == target[2] and have[2] == 0:
                have[2] = 1
            

        return have == [1, 1, 1]
