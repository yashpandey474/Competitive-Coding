class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        #COUNT OF EACH CHARACTER UPTILL THAT INDEX IN ALL THE STRINGS 
        cnt = defaultdict(int)
        for w in words:
            for i, c in enumerate(w):
                cnt[(i,c)] += 1
                

        cache = {}
        def dfs(index, dictInd):
            if index >= len(target):
                return 1

            if dictInd == len(words[0]):
                return 0

            if (index, dictInd) in cache:
                return cache[(index, dictInd)]

            char = target[index]
            #SKIP THE INDEX [IF NONE]
            cache[(index, dictInd)] = dfs(index, dictInd + 1)
            cache[(index, dictInd)] += cnt[(dictInd, char)] * dfs(index + 1, dictInd + 1)
            
            return cache[(index, dictInd)]
        
        result = dfs(0, 0)
        return result%(10**9 + 7)


            
