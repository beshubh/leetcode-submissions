class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        monostack = []
        answer = [0] * len(temps)
        for i in range(len(temps)):
            while monostack and temps[monostack[-1]] < temps[i]:
                answer[monostack[-1]] = i - monostack[-1]
                monostack.pop()
            monostack.append(i)
        return answer
