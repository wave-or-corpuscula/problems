# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/


from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(numbers):
            diff = target - num
            seen[diff] = i
        for i, num in enumerate(numbers):
            if num in seen:
                return [i + 1, seen[num] + 1]


class BinSearchSolution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            s = numbers[left] + numbers[right]
            if s > target:
                right -= 1
            elif s < target:
                left += 1
            else:
                return [left + 1, right + 1]



if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([2,7,11,15], 9),
        ([2,3,4],     6),
        ([-1,0],      -1)
    ]

    for nums, target in tests:
        res = sol.twoSum(nums, target)
        print(res)