# https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/description/?envType=daily-question&envId=2026-02-01

from typing import List


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        
        if len(nums) == 3:
            return sum(nums)
        
        INF = 10 ** 20
        min_costs = [INF, INF]
        for num in nums[1:]:
            if num <= min_costs[0]:
                min_costs[1], min_costs[0] = min_costs[0], num
            elif num < min_costs[1]:
                min_costs[1] = num
        return nums[0] + sum(min_costs)
            

class FasterSolution:
    def minimumCost(self, nums: List[int]) -> int:
        first = nums[0]
        rest = nums[1:]

        rest.sort()
        return first + rest[0] + rest[1]
        


if __name__ == "__main__":
    sol = FasterSolution()
    tests = [
        [1,2,3,12],
        [5,4,3],
        [10,3,1,1],
        [1,5,1,6],
    ]

    for nums in tests:
        res = sol.minimumCost(nums)
        print(res)