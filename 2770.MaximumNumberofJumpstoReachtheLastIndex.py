# https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/description/?envType=daily-question&envId=2026-05-10

from typing import List


class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        """
        
        [1,3,6,4,1,2]
         ^   ^
        
        """
        N = len(nums)
        dp = [-1] * N
        dp[0] = 0

        for i in range(N):
            if dp[i] == -1:
                continue

            for j in range(i + 1, N):
                if abs(nums[j] - nums[i]) <= target:
                    dp[j] = max(dp[j], dp[i] + 1)

        return dp[N - 1]


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([0,2,1,3,4], 1),
        ([1,3,6,4,1,2], 2),
        ([1,3,6,4,1,2], 3),
        ([1,3,6,4,1,2], 0),
    ]
    for nums, target in tests:
        res = sol.maximumJumps(nums, target)
        print(res)