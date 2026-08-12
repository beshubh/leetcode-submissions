class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_ending_here = nums[0]
        min_ending_here = nums[0]
        global_max = nums[0]
        for i in range(1, len(nums)):
            global_max = max(
                global_max,
                max_ending_here * nums[i],
                min_ending_here * nums[i],
                nums[i]
            )
            old_max = max_ending_here
            max_ending_here = max(nums[i], max_ending_here * nums[i], min_ending_here * nums[i])
            min_ending_here = min(nums[i],  min_ending_here * nums[i], old_max * nums[i])
        return max(global_max, max_ending_here)

