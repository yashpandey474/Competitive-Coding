class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        # SELECT A SUBSET OF WORDS THAT CAN BE FORMED USING THE LETTERS SIMULTANEOUSLY
        # AND MAXIMISES THE SCORE

        n = len(words)
        rem = {}
        cache = {}
        def dfs(index, rem, s):
            if index >= n:
                return s

            # NOT TAKE
            res = dfs(index + 1, rem, s)
            
            # CHECK IF CAN TAKE 
            flag = 0
            score_here = 0
            rem1 = {}

            for i in words[index]:
                if i in rem and rem[i] > 0:
                    if i not in rem1:
                        rem1[i] = 0

                    rem[i] -= 1
                    rem1[i] += 1

                else:
                    flag = 1
                    break

                score_here += score[ord(i) - ord('a')]

            # CAN TAKE
            if not flag:
                res = max(res, dfs(index + 1, rem, s + score_here))
            
            for i in rem1:
                rem[i] += rem1[i]

            print(rem, words[index])
            return res

        for i in letters:
            if i not in rem:
                rem[i] = 0

            rem[i] += 1

        print(rem)
        return dfs(0, rem, 0)

            
            