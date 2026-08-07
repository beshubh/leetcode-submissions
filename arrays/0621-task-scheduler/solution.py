import heapq
import collections


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = collections.Counter(tasks).values()
        pq = [-t for t in task_counts]
        heapq.heapify(pq)
        q = collections.deque()
        cycles = 0
        while q or pq:
            cycles += 1
            if pq:
                task_count = -heapq.heappop(pq)
                if task_count - 1 > 0: # 1 > 0 yes
                    q.append((cycles + n, task_count - 1))
            if q and q[0][0] <= cycles:
                heapq.heappush(pq, -q.popleft()[1])
        return cycles
