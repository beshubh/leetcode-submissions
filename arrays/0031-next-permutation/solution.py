class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        smaller_idx = -1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                smaller_idx = i
                break
            
        if smaller_idx == -1:
            nums.reverse()
            return 
        swap_idx = -1 
        for i in range(n - 1, -1, -1):
            if nums[i] > nums[smaller_idx]:
                swap_idx = i
                break
        
        if swap_idx == -1:
            # should be an impossibility?
            return
        nums[smaller_idx], nums[swap_idx] = nums[swap_idx], nums[smaller_idx]
        
        l, r = smaller_idx + 1, n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        
