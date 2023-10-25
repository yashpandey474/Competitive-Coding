class Solution:
    def isPossible(self, nums: List[int]) -> bool:

        if len(nums) < 3:
            return False

        def recursion(index, subsequences):
            if index >= len(nums):
                return

            if len(subsequences) == 0:
                subsequences.append([nums[index]])
                recursion(index + 1, subsequences)

            

            else:
                i = len(subsequences)-1
                while i >= 0:
                    if subsequences[i][-1] == nums[index] - 1:
                        subsequences[i].append(nums[index])
                        break

                    i -= 1

                else:
                    subsequences.append([nums[index]])
                

                recursion(index + 1, subsequences)
                

                    

        subseq = []
        recursion(0, subseq)
        print(subseq)
        for i in subseq:
            if len(i) < 3:
                return False

        return True

            
