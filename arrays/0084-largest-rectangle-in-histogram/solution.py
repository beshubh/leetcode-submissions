class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        # [2, 1, 2, 0]
        # ans = 0
        # [0, ]
        monostack = [] # [ 1, ]
        heights = heights + [0]
        ans  = 0 # 0, 1, 2, 2
        for i in range(len(heights)): # i = 3
            while monostack and heights[monostack[-1]] > heights[i]:  # 1 > 0
                h = heights[monostack.pop()] # 1
                left = -1 if not monostack else monostack[-1] # 1
                w = i - left - 1 # 3 - 1 = 2
                ans = max(ans, h * w)
            monostack.append(i)
        return ans


                
