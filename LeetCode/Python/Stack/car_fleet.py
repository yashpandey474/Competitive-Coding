class Solution:
    
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        def intersect(ele1, ele2):
            time1 = (target - ele1[0])/ele1[1]
            time2 = (target - ele2[0])/ele2[1]

            if time2<=time1:
                return True
            return False

        #CREATE PAIRS OF POSITION AND SPEED
        arr = []
        n = len(position)
        for i in range(n):
            arr.append((position[i], speed[i]))

        #SORT ARRAY ON POSITION
        arr = sorted(arr, key = lambda x: x[0])

        #ITERATE FROM RIGHT
        stack = []
        for i in range(n-1, -1, -1):
            if stack and intersect(stack[-1], arr[i]):
                continue

            else:
                stack.append(arr[i])

        return len(stack)



