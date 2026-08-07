class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left = 0
        pc = collections.Counter(p)
        window = collections.Counter()
        result = [] 
        for right in range(len(s)):
            window[s[right]] += 1
            while right - left + 1 > len(p):
                window[s[left]] -= 1
                left += 1
            if window == pc:
                result.append(left)
        return result
