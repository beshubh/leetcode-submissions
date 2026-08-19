class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        monostack = []
        heights = [0] + heights + [0]
        answer = 0
        for i in range(len(heights)):
            while monostack and heights[monostack[-1]] > heights[i]:
                h = heights[monostack.pop()] 
                left = monostack[-1]
                answer = max(answer, (i - left - 1) * h)
            monostack.append(i)
        return answer
