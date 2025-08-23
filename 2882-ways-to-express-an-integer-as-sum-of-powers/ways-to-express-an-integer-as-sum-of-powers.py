from typing import List

class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9 + 7

        # Precompute powers i^x <= n
        powers = []
        i = 1
        while True:
            p = i ** x
            if p > n:
                break
            powers.append(p)
            i += 1

        # 0/1 knapsack: count subsets summing to n
        dp = [0] * (n + 1)
        dp[0] = 1

        for p in powers:
            for s in range(n, p - 1, -1):
                dp[s] = (dp[s] + dp[s - p]) % MOD

        return dp[n]
