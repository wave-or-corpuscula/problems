# https://leetcode.com/problems/product-of-array-except-self/submissions/1018616048/

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]):
        n = len(nums)
        result = [1] * n

        for i in range(1, n):
            result[i] = result[i - 1] * nums[i - 1]
        
        rightProd = 1
        for i in range(n - 1, -1, -1):
            result[i] *= rightProd
            rightProd *= nums[i]

        return result