class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0]*n
        stack = []

        for i in range(n-1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            
            if not stack:
                answer[i] = 0

            if stack:
                answer[i] = stack[-1] - i

            stack.append(i)
        return answer
