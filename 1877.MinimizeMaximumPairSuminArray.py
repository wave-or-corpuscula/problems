# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/description/?envType=daily-question&envId=2026-01-24

from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        N = len(nums)
        sorted_nums = sorted(nums)
        left, right = sorted_nums[:N//2], sorted_nums[N//2::]
        right.reverse()

        pairs = [l + r for l, r in zip(left, right)]
        return max(pairs)


if __name__ == "__main__":
    sol = Solution()
    tests = [
        [3,5,2,3],
        [3,5,4,2,4,6],
    ]

    for nums in tests:
        res = sol.minPairSum(nums)
        print(res)