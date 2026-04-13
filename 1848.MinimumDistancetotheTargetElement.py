# https://leetcode.com/problems/minimum-distance-to-the-target-element/description/?envType=daily-question&envId=2026-04-13

from typing import List
from math import inf

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        best = inf

        for i, n in enumerate(nums):
            if n == target:
                best = min(best, abs(i - start))

        return best
