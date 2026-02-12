# https://leetcode.com/problems/count-complete-subarrays-in-an-array/description/?envType=problem-list-v2&envId=sliding-window

from typing import List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int: 
        result = 0
        N = len(nums)
        distinct = len(set(nums))

        for length in range(distinct, N + 1):
            for i in range(N - length + 1):
                if len(set(nums[i:i + length])) == distinct:
                    result += 1
        return result


if __name__ == "__main__":
    sol = Solution()
    tests = [
        [1,3,1,2,2],
        [5,5,5,5],
    ]

    for nums in tests:
        res = sol.countCompleteSubarrays(nums)
        print(res)