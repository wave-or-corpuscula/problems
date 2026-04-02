# https://leetcode.com/problems/minimum-cost-to-split-into-ones/description/


class Solution:
    def minCost(self, n: int) -> int:
        return n (n - 1) // 2