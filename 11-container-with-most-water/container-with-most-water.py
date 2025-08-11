from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        best = 0

        while l < r:
            h = height[l] if height[l] < height[r] else height[r]
            best = max(best, h * (r - l))
            # Move the shorter side inward
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return best
