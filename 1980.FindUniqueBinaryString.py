# https://leetcode.com/problems/find-unique-binary-string/description/?envType=daily-question&envId=2026-03-08

from typing import List

from itertools import product


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        set_nums = set(nums)

        for comb in product("01", repeat=len(nums)):
            str_comb = "".join(comb)
            if str_comb not in set_nums:
                return str_comb
            

class InterestingSolution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        result = []
        for i in range(len(nums)):
            if nums[i][i] == '0':
                result.append('1')
            else:
                result.append('0')
        return "".join(result)


if __name__ == "__main__":
    sol = InterestingSolution()
    tests = [
        ["01","10"],
        ["00","01"],
        ["111","011","001"],
    ]
    for nums in tests:
        res = sol.findDifferentBinaryString(nums)
        print(res)