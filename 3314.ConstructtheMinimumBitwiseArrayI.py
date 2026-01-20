# https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/description/?envType=daily-question&envId=2026-01-20

from typing import List


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        def f(x):
            for i in range(1, x + 1):
                if i | (i + 1) == x:
                    return i
            return -1
        
        return [f(num) for num in nums]



if __name__ == "__main__":
    sol =  Solution()
    tests = [
        [11,13,31],
        [2,3,5,7],
    ]

    for nums in tests:
        res = sol.minBitwiseArray(nums)
        print(res)