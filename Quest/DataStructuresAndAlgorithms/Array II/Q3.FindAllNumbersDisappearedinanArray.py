# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/?envType=problem-list-v2&envId=dsa-linear-shoal-array-ii

from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        nums_set = set(nums)
        for i in range(1, len(nums) + 1):
            if i not in nums_set:
                result.append(i)
        return result


if __name__ == "__main__":
    sol = Solution()
    tests = [
        [4,3,2,7,8,2,3,1],
        [1, 1],
    ]

    for test in tests:
        res = sol.findDisappearedNumbers(test)
        print(res)