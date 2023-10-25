class Solution:
    def minSwaps(self, s: str) -> int:

        #KEEP TRACK OF EXTRA CLOSING BRACKETS
        close = 0
        minSwaps = 0

        for i in s:
            if i == '[':
                close -= 1

            else:
                close += 1

            minSwaps = max(minSwaps, close)

        return (minSwaps + 1) // 2
