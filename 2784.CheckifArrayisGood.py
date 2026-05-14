# https://leetcode.com/problems/check-if-array-is-good/description/?envType=daily-question&envId=2026-05-14

from typing import List


class XORSolution:
    def isGood(self, nums: List[int]) -> bool:
        """
        a ^ b ^ c ^ d

        a ^ a ^ b = b

        [5, 5, 4, 3, 2, 1]

        xor = 1 ^ 2 ^ 3 ^ 4 ^ 5 ^ 5

        7 ^ 14 ^ 8 = 7 ^ 7 ^ 2 ^ 2 ^ 2 ^ 2
        
        """

        N = len(nums)

        if N == 1:
            return False

        if N < 3:
            return all(num == 1 for num in nums)

        xor = 0
        best = nums[0]
        for num in nums:
            xor ^= num
            best = max(num, best)
        
        if best != N - 1:
            return False
        
        for i in range(1, N - 1):
            xor ^= i
            print(xor, i)

        if xor == 0:
            return True
        return False
    

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        N = len(nums)
        for i, num in enumerate(nums):
            if i == N - 1:
                return num == N - 1
            if num != (i + 1):
                return False
    

if __name__ == "__main__":
    sol = Solution()
    tests = [
        [7, 14, 8],
        [9, 9],
        [2, 1, 3],
        [1, 3, 3, 2],
        [1, 1],
        [3, 4, 4, 1, 2, 1],
    ]
    for nums in tests:
        res = sol.isGood(nums)
        print(res)