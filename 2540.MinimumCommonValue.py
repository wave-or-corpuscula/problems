# https://leetcode.com/problems/minimum-common-value/description/?envType=daily-question&envId=2026-05-19

from typing import List

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        i = j = 0
        N1 = len(nums1)
        N2 = len(nums2)

        while i <= N1 - 1 and j <= N2 - 1:
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                return nums1[i]
        return -1