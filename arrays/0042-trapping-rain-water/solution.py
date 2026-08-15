class Solution:
    def trap(self, height: List[int]) -> int:
        pre = [0] * len(height)
        suf = [len(height) - 1] * len(height)
        for i in range(1, len(height)):
            if height[i] > height[pre[i - 1]]:
                pre[i] = i
            else:
                pre[i] = pre[i - 1]
        
        for i in range(len(height) - 2, -1, -1):
            if height[i] > height[suf[i + 1]]:
                suf[i] = i
            else:
                suf[i] = suf[i + 1]
        water = 0
        for i in range(1, len(height) - 1):
            h = min(height[pre[i]], height[suf[i]])
            water += (h - height[i])
        return water

