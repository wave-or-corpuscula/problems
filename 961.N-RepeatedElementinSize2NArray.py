# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/description/?envType=daily-question&envId=2026-01-02

from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) / 2
        nums_amount = {}

        for num in nums:
            if nums.count(num) == n:
                return num
            
class SolutionBest:
    def repeatedNTimes(self, nums: List[int]) -> int:
        met = set()
        for num in nums:
            if num in met:
                return num
            met.add(num)
            
    

if __name__ == "__main__":
    tests = [
        [1,2,3,3],
        [2,1,2,5,3,2], 
        [5,1,5,2,5,3,5,4],
    ]
    solution = SolutionBest()
    for test in tests:
        print(solution.repeatedNTimes(test))