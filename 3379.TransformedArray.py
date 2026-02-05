# https://leetcode.com/problems/transformed-array/description/?envType=daily-question&envId=2026-02-05

from typing import List


class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        N = len(nums)
        result = [num if num == 0 else nums[(i + num) % N] for i, num in enumerate(nums)]

        return result