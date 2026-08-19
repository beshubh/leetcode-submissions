class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        data = list(zip(startTime, endTime, profit))
        data.sort(key=lambda x:x[0])
        cache = {}
        def go(i: int):
            if i in cache:
                return cache[i]
            if i >= len(profit):
                return 0
            l, r = i + 1, len(profit) - 1
            while l <= r:
                m = (l + r) // 2
                if data[m][0] < data[i][1]:
                    l = m + 1
                else:
                    r = m - 1
            j = r + 1
            take = data[i][2] + go(j)
            skip = go(i + 1)
            cache[i] = max(take, skip)
            return cache[i]
        return go(0)
