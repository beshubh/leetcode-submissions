import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        tea, ate, eat
        t -> 1
        e -> 1
        a -> 1

        a -> 1
        t -> 1
        e -> 1
        
        counters over each s for s in sts
        space O(n) n => strs, as each s is a lowercase english letter

        """ 
        groups = collections.defaultdict(list)
        for i, s in enumerate(strs):
            counter = collections.Counter(s)
            key = tuple(sorted(counter.items(), key=lambda x:x[0]))
            groups[key].append(i)
        result = []
        for v in groups.values():
            result.append([strs[i] for i in v])
        return result 
