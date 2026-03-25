# https://leetcode.com/problems/first-missing-positive/description/?envType=problem-list-v2&envId=dsa-association-slope-hash

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        for i in range(1, len(nums) + 1):
            if i not in nums:
                return i


class ConstSpaceSolution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)

        for i in range(N):
            if 0 >= nums[i] < N:
                nums[i] = N + 1
        
        for i in range(N):
            num = abs(nums[i])
            if (num > N):
                continue
            num -= 1
            if nums[num] > 0:
                nums[num] *= -1
        
        for i in range(N):
            if nums[i] >= 0:
                return i + 1
        return N + 1


if __name__ == "__main__":
    sol = ConstSpaceSolution()
    tests = [
        [1,2,0],
        [3,4,-1,1],
        [7,8,9,11,12],
    ]

    for nums in tests:
        res = sol.firstMissingPositive(nums)
        print(res)