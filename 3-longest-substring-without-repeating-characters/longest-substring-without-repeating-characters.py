class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index = [0] * 128  # ASCII size
        max_len = 0
        start = 0

        for i, c in enumerate(s):
            start = max(start, index[ord(c)])
            max_len = max(max_len, i - start + 1)
            index[ord(c)] = i + 1

        return max_len
