# https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii/description/?envType=daily-question&envId=2026-01-21

from typing import List


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        B = 32
        INF = 10 ** 20

        def f(x):
            mask = (x << B) - 1
            best = INF

            for i in range(B):
                nmask = ((mask >> i) << i)
                t = (x & nmask)

                if t | (t - 1) == x:
                    best = min(best, t - 1)

            if best >= INF:
                return -1
            return best
        
        return [f(num) for num in nums]


class BestSolution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            res = -1
            d = 1
            while (nums[i] & d) != 0:
                res = nums[i] - d
                d <<= 1
            nums[i] = res
        return nums


    
if __name__ == "__main__":
    sol = Solution()
    tests = [
        [2,3,5,7],
        [11,13,31],
    ]

    for nums in tests:
        res = sol.minBitwiseArray(nums)
        print(res)

