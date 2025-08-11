class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        from functools import lru_cache

        @lru_cache(None)
        def dp(i: int, j: int) -> bool:
            # If pattern consumed, string must also be consumed
            if j == len(p):
                return i == len(s)

            # Check current character match
            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')

            # Handle '*' as zero-or-more of the preceding element
            if j + 1 < len(p) and p[j + 1] == '*':
                # Option 1: skip "x*"
                # Option 2: if first matches, consume one char from s and stay on "x*"
                return dp(i, j + 2) or (first_match and dp(i + 1, j))
            else:
                # Must match current and advance both
                return first_match and dp(i + 1, j + 1)

        return dp(0, 0)
