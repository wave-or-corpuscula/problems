# https://leetcode.com/problems/top-k-frequent-elements/description/

from typing import List

from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ordered_freq = sorted(list(Counter(nums).items()), key=lambda item: item[1], reverse=True)
        return [ordered_freq[i][0] for i in range(k)]
    

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1,1,1,2,2,3], 2),
        ([1], 1),
        ([1,2,1,2,1,2,3,1,3,2], 2),
    ]

    for nums, k in tests:
        res = sol.topKFrequent(nums, k)
        print(res)