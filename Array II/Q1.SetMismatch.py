# https://leetcode.com/problems/set-mismatch/description/?envType=problem-list-v2&envId=dsa-linear-shoal-array-ii

from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        duplicate = None
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                duplicate = num
                break
        set_nums = set(nums)
        for i in range(1, len(nums) + 1):
            if i not in set_nums:
                return [duplicate, i]


class BestSolution: # TODO: Разобраться, почему это работает (понял)
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = [0] * len(nums)
        for i in nums:
            count[i-1] += 1
        return  [count.index(2)+1, count.index(0)+1]
        

if __name__ == "__main__":
    sol = Solution()

    tests = [
        [1,1],
        [3,2,3,4,6,5],
        [1,3,3],
        [1,2,2,4],
        [2,3,2],
        [2,2],

    ]

    for test in tests:
        res = sol.findErrorNums(test)
        print(f"Result: {res}")