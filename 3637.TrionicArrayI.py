# https://leetcode.com/problems/trionic-array-i/description/?envType=daily-question&envId=2026-02-03

from typing import List


class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        N = len(nums)
        if N < 4:
            return False
        
        i = 0
        increase = True
        result = [-1]
        expected = [-1, increase, not increase, increase]
        while i < N - 1:
            if nums[i + 1] > nums[i] and result[-1] is not increase:
                result.append(increase)
            elif nums[i + 1] < nums[i] and result[-1] is not (not increase):
                result.append(not increase)
            elif nums[i + 1] == nums[i]:
                return False
            
            if not all(r == e for r, e in zip(result, expected)) or len(result) > len(expected):
                return False
            
            i += 1

        return result == expected
                


if __name__ == "__main__":
    sol = Solution()
    tests = [
        [4,1,5,2,3],
        [1,3,5,4,2,6],
        [2,1,3],
    ]

    for nums in tests:
        res = sol.isTrionic(nums)
        print(res)