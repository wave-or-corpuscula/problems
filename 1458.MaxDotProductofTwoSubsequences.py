# https://leetcode.com/problems/max-dot-product-of-two-subsequences/description/?envType=daily-question&envId=2026-01-08

from typing import List


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        dp = [[(float("-inf"))] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                product = nums1[i] * nums2[j]

                if i > 0 and j > 0:
                    product += max(0, dp[i - 1][j - 1])
                
                current_max = product
                if i > 0:
                    current_max = max(current_max, dp[i - 1][j])
                if j > 0:
                    current_max = max(current_max, dp[i][j - 1])
                dp[i][j] = current_max
        return dp[n - 1][m - 1]
    
    # TODO: Разобраться в этой проблеме (dp)


if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([2,1,-2,5], [3,0,-6]),
        ([3,-2], [2,-6,7]),
        ([-1,-1], [1,1]),
    ]

    for test in tests:
        res = sol.maxDotProduct(*test)
        print(res)