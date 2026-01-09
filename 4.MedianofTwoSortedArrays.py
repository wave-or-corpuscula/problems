# https://leetcode.com/problems/median-of-two-sorted-arrays/description/

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        all_nums = sorted(nums1 + nums2)
        ind = len(all_nums) // 2
        if len(all_nums) % 2:
            return all_nums[ind]
        return sum(all_nums[ind - 1:ind + 1]) / 2
    

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1,3],[2]),
        ([1,2],[3,4]),
        ([], []),
        ([1], []),
        ([1], [1]),
    ]

    for test in tests:
        print(sol.findMedianSortedArrays(*test))