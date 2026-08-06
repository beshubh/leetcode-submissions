class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        used = [False] * len(nums)
        output = []
        current = []
        def backtrack(i: int):
            if i >= len(nums):
                output.append(current.copy())
                return
            # choose it if not chosen
            if not used[i]:
                used[i] = True
                current.append(nums[i])
                backtrack(i + 1)
                current.pop()
                used[i] = False
            backtrack(i + 1)
        backtrack(0)
        return output
