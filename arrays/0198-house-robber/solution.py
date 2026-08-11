class Solution:
    def rob(self, nums: List[int]) -> int:

        def go(i: int):
            if i >= len(nums):
                return 0
            c1 = nums[i] + go(i + 2)
            c2 = go(i + 1) 
            return max(c1, c2)
        
        dp = [0] * (len(nums) + 2)
        for i in range(len(nums), -1, -1):
            if i < len(nums):
                dp[i] = max(dp[i + 1], dp[i + 2] + nums[i])
            else:
                dp[i] = dp[i + 1]
        return dp[0]
