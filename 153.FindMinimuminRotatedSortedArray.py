# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/?envType=daily-question&envId=2026-05-15

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]


if __name__ == "__main__":
    sol = Solution()
    tests = [
        [3,4,5,1,2],
        [4,5,6,7,0,1,2],
        [11,13,15,17],
    ]
    for nums in tests:
        res = sol.findMin(nums)
        print(res)