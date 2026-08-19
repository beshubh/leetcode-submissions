import collections


class Solution:

    def diff_by_one(self, a, b):
        if len(a) != len(b):
            return False
        diff = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                diff += 1
        return diff == 1
 
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = collections.defaultdict(list)
        if endWord not in wordList:
            return 0
        for u in wordList:
            for v in wordList:
                if self.diff_by_one(u, v):
                    graph[u].append(v)
        
        for u in wordList:
            if self.diff_by_one(beginWord, u):
                graph[beginWord].append(u)
        
        length = 0
        q = collections.deque([beginWord])
        seen = set()
        while q:
            for _ in range(len(q)):
                u = q.popleft()
                if u == endWord:
                    return length + 1 
                for v in graph[u]:
                    if v not in seen:
                        seen.add(v)
                        q.append(v)
            length += 1
        return 0



        
