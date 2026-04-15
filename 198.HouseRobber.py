# https://leetcode.com/problems/house-robber/description/

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [0] * (N + 2)

        for i, money in zip(range(2, N + 2), nums):
            dp[i] = max(dp[i - 2] + money, dp[i - 1])
        
        return dp[-1]
    
class SolutionConstSpace:
    def rob(self, nums: List[int]) -> int:
        first = 0
        second = 0

        for num in nums:
            robbed = max(first + num, second)
            first = second
            second = robbed
        return second


if __name__ == "__main__":
    sol = Solution()
    tests = [
        [2,1,1,2],
        [1,2,3,1],
        [2,7,9,3,1],
    ]
    for n in tests:
        res = sol.rob(n)
        print(res)