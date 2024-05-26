class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)


        # STORE THE ACTUAL SCHEDULE
        schedule = [-1 for i in range(n)]

        # SORT THE DECK
        deck = sorted(deck)

        # SIMULATE THE REVEAL
        queue = [i for i in range(n)]

        # CURRENT ELEMENT
        count = 0
        while count < n:
            # NEXT ELEMENT AT THE CURRENT POPPED INDEX IN SCHEDULE
            schedule[queue.pop(0)] = deck[count]
            count += 1
            # ADD NEXT CARD TO BOTTOM
            if queue:
                queue.append(queue.pop(0))

        return schedule