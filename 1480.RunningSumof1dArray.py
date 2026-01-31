# https://leetcode.com/problems/running-sum-of-1d-array/description/

from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        ### Это норм, но нижний - быстрее
        
        # N = len(nums)
        
        # running_sum = [nums[0]] * N
        # for i in range(1, N):
        #     running_sum[i] = running_sum[i - 1] + nums[i]
        
        # return running_sum

        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums