import heapq
import collections


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        pq = []
        task_counts = list(sorted(list(collections.Counter(tasks).values())))
        q = collections.deque(task_counts)
        cycles = 0 # 6
        while q or pq:
            cycles += 1
            if q:
                task_count = q.pop() # 2
                if task_count - 1 > 0: # 1 > 0 yes
                    heapq.heappush(pq, (cycles + n, -(task_count - 1)))
            if pq and pq[0][0] <= cycles: # 4 <= 4 yes
                tsk = -heapq.heappop(pq)[1]
                if q and q[-1] <= tsk:
                    q.append(tsk)
                elif q:
                    q.appendleft(tsk)
                else:
                    q.append(tsk)

        return cycles
