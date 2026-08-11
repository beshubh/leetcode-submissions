class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0]*len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                top = stack.pop()
                answer[top[1]] = i - top[1]
            stack.append((t, i)) 
        return answer
