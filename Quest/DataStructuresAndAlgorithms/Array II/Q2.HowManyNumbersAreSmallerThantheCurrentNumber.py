# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/?envType=problem-list-v2&envId=dsa-linear-shoal-array-ii

from typing import List

from collections import Counter


class BrutForceSolution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    result[i] += 1
        return result
    

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        mas = []
        sorted_mas = sorted(nums)
        db = {}

        for i, num in enumerate(sorted_mas):
            if num not in db:
                db[num] = i
        for num in nums:
            mas.append(db[num])
        return mas


if __name__ == "__main__":
    sol = Solution()
    # sol = BrutForceSolution()

    tests = [
        [8,1,2,2,3],
        [6,5,4,8],
        [7,7,7,7],
    ]

    for test in tests:
        res = sol.smallerNumbersThanCurrent(test)
        print(res)