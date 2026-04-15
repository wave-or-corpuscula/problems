# https://leetcode.com/problems/house-robber-ii/description/

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def _rob(money: List[int]) -> int:
            first = 0
            second = 0

            for mon in money:
                robbed = max(first + mon, second)
                first = second
                second = robbed

            return second
        
        return max(_rob(nums[1:]), _rob(nums[:-1]))


if __name__ == "__main__":
    sol = Solution()
    tests = [
        [2,3,2],
        [1,2,3,1],
        [1,2,3],
        [1],
    ]
    for n in tests:
        res = sol.rob(n)
        print(res)
        