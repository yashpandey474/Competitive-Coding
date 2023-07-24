'''
PROBLEM: ALWAYS CHOOSE A CARD FROM LEFT END OR RIGHT END
CHOOSE TOTAL K CARDS

-> KEEP A SLIDING WINDOW OF SIZE N - K
-> SUM OF ELEMENTS OUTISDE THE WINDOW IS CURRENT SUM POSSIBLE
-> KEEP MOVING IT FORWARD AND KEEP IT AS SIZE  N - K
-> ADD STARTING ELEMENT TO SUM; MOVE START FORWARD
-> REMOVE ENDING ELEMENT FROM SUM; MOVE END FORWARD
-> RETURN MAX OF SUCH SUMS
'''
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        #FIND THE WINDOW WHERE REMAINING ELEMENTS HAVE MAXIUM SUM
        n = len(cardPoints)
        left, right = 0, n - k
        current_sum = sum(cardPoints[right:])
        max_sum = current_sum

        while right < n:
            current_sum += cardPoints[left]
            current_sum -= cardPoints[right]
            max_sum = max(max_sum, current_sum)
            right += 1
            left += 1

        return max_sum
