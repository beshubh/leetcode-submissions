class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        data = list(zip(startTime, endTime, profit))
        data.sort(key=lambda x:x[0])
        n = len(data) 
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            l, r = i + 1, n - 1
            while l <= r:
                m = (l + r) // 2
                if data[m][0] < data[i][1]:
                    l = m + 1
                else:
                    r = m - 1
            j = r + 1
            take = data[i][2] + dp[j]
            skip = dp[i + 1]
            dp[i] = max(take, skip)
        return dp[0]

