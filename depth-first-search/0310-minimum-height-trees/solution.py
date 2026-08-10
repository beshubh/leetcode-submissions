import collections


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = collections.defaultdict(list)
        edges_count = {}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        for src, neighbors in graph.items():
            edges_count[src] = len(neighbors)
        leaves = collections.deque()
        for src in edges_count:
            if edges_count[src] == 1:
                leaves.append(src)
        while leaves:
            if n <= 2:
                return list(leaves)
            for _ in range(len(leaves)):
                node = leaves.popleft()
                n -= 1
                for nei in graph[node]:
                    edges_count[nei] -= 1
                    if edges_count[nei] == 1:
                        leaves.append(nei)
            
