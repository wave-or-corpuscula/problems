# https://leetcode.com/problems/xor-after-range-multiplication-queries-ii/description/?envType=daily-question&envId=2026-04-09

from functools import reduce
from operator import xor
from math import isqrt
from collections import defaultdict

from typing import List


class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        B = isqrt(n) + 1

        buckets = defaultdict(lambda: defaultdict(dict))

        for l, r, k, v in queries:
            if k > B:
                i = l
                while i <= r:
                    nums[i] = nums[i] * v % MOD
                    i += k
            else:
                mod = l % k

                start = (l - mod) // k
                end = (r - mod) // k

                d = buckets[k][mod]

                d[start] = d.get(start, 1) * v % MOD
                inv_v = pow(v, MOD - 2, MOD)
                d[end + 1] = d.get(end + 1, 1) * inv_v % MOD

        for k in buckets:
            for mod in buckets[k]:
                d = buckets[k][mod]

                cur = 1
                i = mod
                pos = 0

                while i < n:
                    if pos in d:
                        cur = cur * d[pos] % MOD

                    nums[i] = nums[i] * cur % MOD

                    i += k
                    pos += 1

        return reduce(xor, nums)