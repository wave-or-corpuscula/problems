# https://leetcode.com/problems/rotate-function/description/?envType=daily-question&envId=2026-05-01

from typing import List

class BrutforceSolution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        """
        
        [4,3,2,6]
        [6,4,3,2]
        [2,6,4,3]
        [3,2,6,4]
        
        """
        
        N = len(nums)
        best = float("-inf")
        for i in range(N):
            arr = nums[-i:] + nums[:-i]
            f = sum(i * n for i, n in enumerate(arr))
            best = max(f, best)
        
        return best
    

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        
        """

        [4,3,2,6] -> (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6)

        [6,4,3,2] -> (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2)


        [2,6,4,3] -> (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3)
        [3,2,6,4] -> (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4)

        """

        N = len(nums)
        S = sum(nums)
        F0 = sum(a * i for a, i in enumerate(nums))

        best = F0
        F = F0
        for i in range(N):
            F = F + S - nums[N - 1 - i] * N
            best = max(F, best)

        return best





if __name__ == "__main__":
    sol = Solution()
    tests = [
        [4,3,2,6],
        [100],
    ]

    for nums in tests:
        res = sol.maxRotateFunction(nums)
        print(res)