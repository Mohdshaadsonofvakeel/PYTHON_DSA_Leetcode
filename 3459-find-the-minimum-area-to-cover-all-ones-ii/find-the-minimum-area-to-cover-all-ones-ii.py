from typing import List
from math import inf

class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def area(i1, j1, i2, j2):
            x1, y1 = inf, inf
            x2, y2 = -inf, -inf
            for i in range(i1, i2 + 1):
                for j in range(j1, j2 + 1):
                    if grid[i][j] == 1:
                        x1 = min(x1, i)
                        y1 = min(y1, j)
                        x2 = max(x2, i)
                        y2 = max(y2, j)
            if x1 == inf:
                return 0
            return (x2 - x1 + 1) * (y2 - y1 + 1)

        ans = inf

        # Two horizontal splits
        for i1 in range(m - 1):
            for i2 in range(i1 + 1, m - 1):
                a1 = area(0, 0, i1, n - 1)
                a2 = area(i1 + 1, 0, i2, n - 1)
                a3 = area(i2 + 1, 0, m - 1, n - 1)
                ans = min(ans, a1 + a2 + a3)

        # Two vertical splits
        for j1 in range(n - 1):
            for j2 in range(j1 + 1, n - 1):
                a1 = area(0, 0, m - 1, j1)
                a2 = area(0, j1 + 1, m - 1, j2)
                a3 = area(0, j2 + 1, m - 1, n - 1)
                ans = min(ans, a1 + a2 + a3)

        # Horizontal then vertical (top part)
        for i in range(m - 1):
            for j in range(n - 1):
                a1 = area(0, 0, i, j)
                a2 = area(0, j + 1, i, n - 1)
                a3 = area(i + 1, 0, m - 1, n - 1)
                ans = min(ans, a1 + a2 + a3)

        # Horizontal then vertical (bottom part)
        for i in range(m - 1):
            for j in range(n - 1):
                a1 = area(0, 0, i, n - 1)
                a2 = area(i + 1, 0, m - 1, j)
                a3 = area(i + 1, j + 1, m - 1, n - 1)
                ans = min(ans, a1 + a2 + a3)

        # Vertical then horizontal (left part)
        for j in range(n - 1):
            for i in range(m - 1):
                a1 = area(0, 0, i, j)
                a2 = area(i + 1, 0, m - 1, j)
                a3 = area(0, j + 1, m - 1, n - 1)
                ans = min(ans, a1 + a2 + a3)

        # Vertical then horizontal (right part)
        for j in range(n - 1):
            for i in range(m - 1):
                a1 = area(0, 0, m - 1, j)
                a2 = area(0, j + 1, i, n - 1)
                a3 = area(i + 1, j + 1, m - 1, n - 1)
                ans = min(ans, a1 + a2 + a3)

        return ans
