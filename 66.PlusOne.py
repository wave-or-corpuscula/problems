# https://leetcode.com/problems/plus-one/description/?envType=daily-question&envId=2026-01-01

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            if carry == 0:
                return digits
            plus_one = digits[i] + carry
            if plus_one < 10:
                carry = 0
            digits[i] = plus_one % 10
        return [1] + digits if carry else digits 
            

if __name__ == "__main__":
    tests = [
        [1,2,3],
        [4,3,2,1],
        [9],
        [0],
        [8,9,9,9],
        [9,9,9,9,9,9,9,9,9,9,9,9]
    ]
    sol = Solution()
    for test in tests:
        res = sol.plusOne(test)
        print(res)