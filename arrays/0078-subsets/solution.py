class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        current = []
        result = []

        def go(i: int):
            if i >= len(nums):
                result.append(current.copy())
                return
            # take it
            if i not in seen:
                seen.add(i)
                current.append(nums[i])
                go(i + 1)
                seen.remove(i)
                current.pop()
            
            go(i + 1)
        go(0)
        return result


