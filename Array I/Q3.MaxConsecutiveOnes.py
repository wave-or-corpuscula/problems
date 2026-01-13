# https://leetcode.com/problems/max-consecutive-ones/description/?envType=problem-list-v2&envId=dsa-linear-shoal-array-i

from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_seq = 0
        only_ones = 0
        for n in nums:
            if n == 1:
                only_ones += 1
            else:
                max_seq = max(max_seq, only_ones)
                only_ones = 0
        return max(max_seq, only_ones)