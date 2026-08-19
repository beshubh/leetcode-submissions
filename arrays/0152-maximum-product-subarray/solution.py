class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        global_max = nums[0]
        current_max = nums[0]
        current_min = nums[0]
        for i in range(1, len(nums)):
            global_max = max(
                global_max,
                current_max*nums[i],
                current_min*nums[i],
                nums[i]
            )
            temp = current_max
            current_max = max(current_max * nums[i], nums[i], current_min * nums[i])
            current_min = min(current_min * nums[i], nums[i], temp * nums[i])
        return max(global_max, current_max, current_min)
