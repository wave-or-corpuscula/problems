# https://leetcode.com/problems/minimum-distance-between-three-equal-elements-ii/description/?envType=daily-question&envId=2026-04-11

from typing import List
from math import inf
from collections import defaultdict


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        """
        
        [1,1,2,3,2,1,1,1,2]
                   ^ ^ ^
        
        """
        f = defaultdict(list)

        for index, x in enumerate(nums):
            f[x].append(index)

        best = inf
        for key in f.keys():
            L = f[key]
            for i, j, k in zip(L, L[1:], L[2:]):
                best = min(best, abs(j - i) + abs(k - j) + abs(i - k))
        
        return -1 if best == inf else best
        
        



if __name__ == "__main__":
    sol = Solution()
    tests = [
        [1,2,1,1,3],
        [1,1,2,3,2,1,2],
        [1],
    ]

    for nums in tests:
        res = sol.minimumDistance(nums)
        print(res)