# https://leetcode.com/problems/longest-balanced-subarray-i/description/?envType=daily-question&envId=2026-02-10

from typing import List

from collections import Counter


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for l in range(n):
            evens = set()
            odds = set()
            for r in range(l, n):
                if nums[r] % 2 == 0:
                    evens.add(nums[r])
                else:
                    odds.add(nums[r])

                if len(evens) == len(odds):
                    ans = max(ans, r - l + 1)

        return ans
    
class FastestSolution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        seen = set()
        for i in range(n):
            seen.clear()
            balance = 0
            if res > n - i:
                break
            for j in range(i, n):
                num = nums[j]
                if num not in seen: 
                    if num % 2:
                        balance -= 1
                    else:
                        balance += 1
                    seen.add(num)
                if balance == 0:
                    res = max(res, j - i + 1)
        
        return res


if __name__ == "__main__":
    sol = Solution()
    tests = [
        [6, 6],
        [22,22,26,25,10],
        [2,5,4,3],
        [3,2,2,5,4],
        [1,2,3,2],
    ]

    for nums in tests:
        res = sol.longestBalanced(nums)
        print(res)