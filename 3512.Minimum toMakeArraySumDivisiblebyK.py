# https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/description/

from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(nums) % k