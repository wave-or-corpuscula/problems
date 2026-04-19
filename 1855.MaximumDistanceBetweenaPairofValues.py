# https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/description/?envType=daily-question&envId=2026-04-19

from typing import List


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = j = 0
        N1 = len(nums1)
        N2 = len(nums2)

        best = 0
        while i < N1 and j < N2:
            while j < N2 and nums2[j] >= nums1[i]:
                best = max(best, j - i)
                j += 1
            else:
                i += 1

        return best
            


if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([55,30,5,4,2], [100,20,10,10,5]),
        ([2,2,2], [10,10,1]),
        ([30,29,19,5], [25,25,25,25,25]),
    ]

    for n1, n2 in tests:
        res = sol.maxDistance(n1, n2)
        print(res)