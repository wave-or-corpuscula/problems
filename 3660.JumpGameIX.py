# https://leetcode.com/problems/jump-game-ix/description/?envType=daily-question&envId=2026-05-07

from math import inf
from typing import List


class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        """

        [2,1,3]
           ^

        [2,3,1]
           ^

        [1,2,3,8,7,1] -> [1,8,8,8,8,8]

        """
        N = len(nums)

        ans = [0] * N
        # [value, index]
        prev_max = [(0, 0)] * N

        prev = (-inf, -1)
        for i, value in enumerate(nums):
            if value > prev[0]:
                prev = (value, i)
            prev_max[i] = prev

        def process(r: int, right_min: float, right_max: float) -> None:
            p_max, pivot_index = prev_max[r]
            curr_max = p_max if p_max <= right_min else right_max

            next_right_min = min(p_max, right_min)
            for i in range(pivot_index, r + 1):
                ans[i] = curr_max
                next_right_min = min(next_right_min, nums[i])

            if pivot_index == 0:
                return

            process(pivot_index - 1, next_right_min, curr_max)

        process(N - 1, inf, 0)

        return ans