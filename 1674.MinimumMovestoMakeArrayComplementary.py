# https://leetcode.com/problems/minimum-moves-to-make-array-complementary/description/?envType=daily-question&envId=2026-05-13
from collections import defaultdict
from typing import List


class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        """
        
        [1,2,4,3]      4
        
        """
        best = N = len(nums)
        d = defaultdict(int)
        delta = defaultdict(int)
        maxTotal = 2

        for index in range(N // 2):
            maxOne = max(nums[index] + limit, nums[-(index + 1)] + limit)
            minOne = min(nums[index] + 1, nums[-(index + 1)] + 1)
            total = nums[index] + nums[-(index + 1)]
            if maxTotal < total:
                maxTotal = total

            d[total] += 1

            delta[minOne] -= 1
            delta[maxOne + 1] += 1
        
        current = N
        for total in range(2, maxTotal + 1):
            current += delta[total]
            best = min(best, current - d[total])
        return best



if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1,2,4,3], 4),
        ([1,2,2,1], 2),
        ([1,2,1,2], 2),
    ]
    for n, lim in tests:
        res = sol.minMoves(n, lim)
        print(res)