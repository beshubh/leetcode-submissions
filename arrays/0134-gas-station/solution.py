class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        ret = -1
        # gas = [1,2,3,4,5], cost = [3,4,5,1,2]
        # output = 3
        # cost = 
        if sum(gas) < sum(cost):
            return -1
        tank, start, total = 0, 0, 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff
            tank += diff
            if tank < 0:
                start = i + 1
                tank = 0
        return start if total >= 0 else -1
