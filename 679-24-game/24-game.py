from typing import List

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def dfs(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6

            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i != j:
                        a, b = nums[i], nums[j]
                        next_nums = [nums[k] for k in range(len(nums)) if k != i and k != j]
                        for op in self.compute(a, b):
                            if dfs(next_nums + [op]):
                                return True
            return False

        return dfs([float(x) for x in cards])

    def compute(self, a, b):
        results = [a + b, a - b, b - a, a * b]
        if b != 0:
            results.append(a / b)
        if a != 0:
            results.append(b / a)
        return results
