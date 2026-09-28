class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        s = 0
        best = 0
        first = {0: -1}
        for i, n in enumerate(nums):
            s += 1 if n == 1 else -1
            if s in first:
                best = max(best, i - first[s])
            else:
                first[s] = i
        return best
