# https://leetcode.com/problems/minimum-distance-between-three-equal-elements-i/description/?envType=daily-question&envId=2026-04-10

from typing import List

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        N = len(nums)
        if N < 3:
            return -1
        
        best = float("inf")

        for i in range(N - 2):
            for j in range(i + 1, N - 1):
                for k in range(j + 1, N):
                    if nums[i] == nums[j] == nums[k]:
                        best = min(best, abs(i - j) + abs(j - k) + abs(k - i))
        return best


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