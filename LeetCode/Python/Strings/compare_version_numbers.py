class Solution:
    def getNextNumber(self, v1, i):
        number = 0
        while i<len(v1) and v1[i] != '.':
            number = number*10 + int(v1[i])
            i+=1

        return number, i
    def compareVersion(self, version1: str, version2: str) -> int:
        i = 0
        j = 0
        while i<len(version1) and j<len(version2):
            num_a, i = self.getNextNumber(version1, i)
            num_b, j = self.getNextNumber(version2, j)

            if num_a < num_b:
                return -1
            
            if num_b > num_a:
                return 1
            
            if i<len(version1) and version1[i] == '.':
                i+=1
            if j<len(version2) and version2[j] == '.':
                j+=1

        return 0
