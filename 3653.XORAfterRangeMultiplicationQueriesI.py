# https://leetcode.com/problems/xor-after-range-multiplication-queries-i/description/?envType=daily-question&envId=2026-04-08

from typing import List

from functools import reduce
from operator import xor


class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        """
        
        queries[i] = [li, ri, ki, vi].
        
        """
        MOD = 10 ** 9 + 7
        for idx, n, k, v in queries:
            while idx <= n:
                nums[idx] = nums[idx] * v % MOD
                idx += k

        return reduce(xor, nums)


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1,1,1],     [[0,2,1,4]]),
        ([2,3,1,5,4], [[1,4,2,3],[0,2,1,2]]),
    ]

    for n, q in tests:
        res = sol.xorAfterQueries(n, q)
        print(res)