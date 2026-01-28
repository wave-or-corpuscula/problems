# https://leetcode.com/problems/minimum-absolute-difference/?envType=daily-question&envId=2026-01-26

from typing import List

from collections import defaultdict


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()

        N = len(arr)
        diffs = defaultdict(list)
        min_diff = 10 ** 7

        for i in range(0, N - 1):
            diff = abs(arr[i + 1] - arr[i])
            if diff <= min_diff:
                diffs[diff].append([arr[i], arr[i + 1]])
                min_diff = diff
        return diffs[min_diff]
    
class BetterMemorySolution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()

        N = len(arr)
        ans = []
        min_diff = 10 ** 7

        for i in range(0, N - 1):
            diff = abs(arr[i + 1] - arr[i])
            if diff < min_diff:
                ans = []
                min_diff = diff
            if diff == min_diff:
                ans.append([arr[i], arr[i + 1]])
        return ans


if __name__ == "__main__":
    sol = Solution()
    tests = [
        [4,2,1,3],
        [1,3,6,10,15],
        [3,8,-10,23,19,-4,-14,27],
    ]

    for arr in tests:
        res = sol.minimumAbsDifference(arr)
        print(res)