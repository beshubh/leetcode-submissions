class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        result = ""
        n = len(s)
        for i in range(len(s)):
            # odd length
            left, right = i - 1, i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left + 1 > longest:
                longest = right - left + 1
                result = s[left + 1:right]
            
            # even length
            left, right = i, i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
        
            if right - left + 1 > longest:
                longest = right - left + 1
                result = s[left + 1:right]
        return result
             
