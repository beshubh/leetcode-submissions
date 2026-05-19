class Solution:

    def is_palindrome(self, s, i , j):
        while i <= j:
            if s[i] != s[j]:
                return False
            i, j = i + 1, j - 1
        return True

    def longestPalindrome(self, s: str) -> str:
        best = (0, 0)
        if len(s) <= 1:
            return s
        start = 0
        max_len = 0

        def expand(left, right):
            nonlocal start, max_len
            while left >= 0 and right < len(s) and s[left] == s[right]:
                curr_len = right - left + 1
                if curr_len > max_len:
                    max_len = curr_len
                    start = left
                left -= 1
                right += 1

        for i in range(len(s)):
            expand(i, i) # odd
            expand(i, i + 1) # even
        return s[start:start + max_len]
    
