'''
1. MAINTAIN HEAP OF ELEMENTS
2. MAINTAIN HASHMAP OF FREQUENCY OF ELEMENTS
3. GET LOWEST VALUE FROM HEAP
4. POP THE ELEMENT FROM HEAP AND ITERATE FOR GROUP SIZE FROM CURRENT
5. IF FREQUENCY DOES NOT REACH 0; PUSH THE ELEMENT BACK
'''
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        #IF CANNOT BE DIVIDED
        if len(hand)%groupSize:
            return False

        #CREATE A HASH MAP OF FREQUENCY
        map_freq = {}
        heap = []

        for i in hand:
            if i in map_freq:
                #INCREMENT THE FREQUENCY
                map_freq[i] += 1
            
            else:
                #TO GET THE MINIMUM VALUES
                heapq.heappush(heap, i)
                map_freq[i] = 1

        print(map_freq)
        print(heap)
        #FOR ALL GROUPS
        for i in range(len(hand)//groupSize):
            if not heap:
                return False
            #FIRST ELEMENT OF THE GROUP
            current = heap[0]
            print("CURRENT = ", current)
            #ITERATE FOR NEXT ELEMENTS
            for j in range(current, current+groupSize):
                ele = heapq.heappop(heap)
                #ELEMENT NOT PRESENT
                if j not in map_freq or map_freq[j] == 0:
                    print("NOT FOUND: ", j)
                    return False
                #DECREMENT COUNT OF ELEMENT
                print("FOUND: ", j)
                map_freq[j]-=1

                if map_freq[j] != 0:
                    heapq.heappush(heap, ele)

        return True

                

                


        return formed == groupSize
