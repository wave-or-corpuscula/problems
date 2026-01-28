# https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/description/?envType=problem-list-v2&envId=sliding-window

from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        N = len(nums)
        inverse_len = 3
        opcnt = 0

        for i in range(N - inverse_len + 1):
            if nums[i] == 0:
                opcnt += 1
                for j in range(i, i + inverse_len):
                    nums[j] ^= 1
        
        return opcnt if all(nums) else -1
    

if __name__ == "__main__":
    sol = Solution()
    tests = [
        # [0,0,0,0,0,0],
        [0,1,1,1,0,0],
        [0,1,1,1],
    ]

    for test in tests:
        print(sol.minOperations(test))