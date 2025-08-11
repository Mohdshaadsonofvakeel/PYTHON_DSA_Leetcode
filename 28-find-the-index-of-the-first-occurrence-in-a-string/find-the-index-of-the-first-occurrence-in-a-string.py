class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)

        # Edge case: empty needle
        if m == 0:
            return 0

        # Slide over haystack with a window of size m
        for i in range(n - m + 1):
            if haystack[i:i + m] == needle:
                return i

        return -1
