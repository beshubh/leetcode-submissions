import collections


class Solution:

    def _window_include_t(self, window, t_count):
        for c in t_count.keys():
            if c not in window:
                return False
            if window[c] < t_count[c]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        t_count = collections.Counter(t)
        window = collections.Counter()
        have = 0
        need = len(t_count)
        result = (0, 1e9)
        left = 0
        for right in range(len(s)):
            ch = s[right]
            window[ch] += 1
            if window[ch] == t_count[ch]:
                have += 1
            while have >= need:
                window[s[left]] -= 1
                if right - left < result[1] - result[0]:
                    result = (left, right)
                if window[s[left]] < t_count[s[left]]:
                    have -= 1
                left += 1
        if result == (0, 1e9):
            return ""
        return s[result[0]: result[1] + 1]
