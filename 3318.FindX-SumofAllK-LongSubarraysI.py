# https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/description/?envType=problem-list-v2&envId=sliding-window

from typing import List

from collections import Counter


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        
        def xsum(ns: List[int]) -> int:
            freq = list(Counter(ns).items())
            freq.sort(key=lambda item: (item[1], item[0]), reverse=True)
            return sum(key * value for key, value in freq[:x])

        N = len(nums)
        result = []
        for i in range(N - k + 1):
            subarray = nums[i:i + k]
            if k <= x:
                result.append(sum(subarray))
            else:
                result.append(xsum(subarray))
        return result


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1,1,2,2,3,4,2,3], 6, 2),
        ([3,8,7,8,7,5], 2, 2),
    ]
    for nums, k, x in tests:
        res = sol.findXSum(nums, k, x)
        print(res)