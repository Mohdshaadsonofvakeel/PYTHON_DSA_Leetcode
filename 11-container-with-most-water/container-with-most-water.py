from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        best = 0

        while l < r:
            if height[l] < height[r]:
                h = height[l]
                best = max(best, h * (r - l))
                l += 1
                # Skip all positions that are ≤ the limiting height h
                while l < r and height[l] <= h:
                    l += 1
            else:
                h = height[r]
                best = max(best, h * (r - l))
                r -= 1
                # Skip all positions that are ≤ the limiting height h
                while l < r and height[r] <= h:
                    r -= 1

        return best
