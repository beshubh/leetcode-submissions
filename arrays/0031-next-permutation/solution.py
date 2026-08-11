class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot = i
                break
        if pivot == -1:
            nums.sort()
            return
        swap_idx = -1
        for i in range(pivot + 1, len(nums)):
            if swap_idx == -1:
                if nums[i] > nums[pivot]:
                    swap_idx = i
            else:
                if nums[i] > nums[pivot] and nums[i] < nums[swap_idx]:
                    swap_idx = i
        nums[pivot], nums[swap_idx] = nums[swap_idx], nums[pivot]
        for i in range(pivot + 1, len(nums)):
            for j in range(pivot + 1, len(nums) - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        
