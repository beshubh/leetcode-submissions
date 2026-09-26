class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        current = []
        candidates.sort()
        def go(i: int, running_sum: int):
            if running_sum == target:
                result.append(current.copy())
                return
            if running_sum > target:
                return
            if i >= len(candidates):
                return
            current.append(candidates[i])
            go(i, running_sum + candidates[i])
            current.pop()
            j = i
            while j < len(candidates) and candidates[i] == candidates[j]:
                j += 1
            go(j, running_sum)
        go(0, 0)
        return result

            

