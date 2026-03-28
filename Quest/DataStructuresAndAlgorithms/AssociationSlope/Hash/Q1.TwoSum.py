# https://leetcode.com/problems/two-sum/description/?envType=problem-list-v2&envId=dsa-association-slope-hash

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, val in enumerate(nums):
            if val not in seen:
                diff = target - val
                seen[diff] = i
            else:
                return [seen[val], i]