class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        monostack = []
        heights = [0] + heights + [0]
        answer = 0
        for i in range(len(heights)):
            h = heights[i]
            while monostack and heights[monostack[-1]] > h:
                left = monostack.pop()
                height = heights[left]
                width = i - monostack[-1] - 1
                answer = max(height * width, answer)
            monostack.append(i)
        return answer
