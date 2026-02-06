# https://leetcode.com/problems/minimum-removals-to-balance-array/description/?envType=daily-question&envId=2026-02-06

from typing import List


class Solution:
    def minRemovals(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        l = 0
        max_len = 1

        for r in range(n):
            while nums[r] > k * nums[l]:
                l += 1
            max_len = max(max_len, r - l + 1)

        return n - max_len


class BetterSolution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        
        for r in range(len(nums)):
            if nums[r] > nums[l] * k:
                l += 1
        return l


if __name__ == "__main__":
    sol = Solution()

    tests = [
        [1,6,2,9],
        [1,34,23],
        [2,1,5],
        [4,6],
    ]