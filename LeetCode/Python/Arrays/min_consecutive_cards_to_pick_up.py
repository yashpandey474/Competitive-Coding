class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        map_cards = {}
        min_dist = float('inf')

        for i in range(len(cards)):
            if cards[i] not in map_cards:
                map_cards[cards[i]] = i

            else:
                min_dist = min(min_dist,i - map_cards[cards[i]] + 1)
                map_cards[cards[i]] = i
        
        if min_dist == float('inf'):
            return -1
        
        return min_dist
