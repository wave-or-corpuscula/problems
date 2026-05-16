# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/?envType=daily-question&envId=2026-05-16

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        def dnc(left: int, right: int) -> int:
            if left == right:
                return nums[left]

            if nums[left] < nums[right]:
                return nums[left]

            m = (left + right) // 2

            return min(dnc(left, m), dnc(m + 1, right))

        return dnc(0, len(nums) - 1)