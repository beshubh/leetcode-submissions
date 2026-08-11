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
        swap = -1
        for i in range(pivot + 1, len(nums)):
            if nums[i] > nums[pivot]:
                if swap == -1:
                    swap = i
                elif nums[i] <= nums[swap]:
                    swap = i
        nums[pivot], nums[swap] = nums[swap], nums[pivot]
        left, right = pivot + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


