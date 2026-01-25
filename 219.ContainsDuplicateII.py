# https://leetcode.com/problems/contains-duplicate-ii/description/?envType=problem-list-v2&envId=sliding-window

from typing import List

from collections import defaultdict


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indices_map = defaultdict(list)

        for i, num in enumerate(nums):
            indices_map[num].append(i)
        
        for _, indxs in indices_map.items():
            for i in range(len(indxs) - 1):
                if indxs[i + 1] - indxs[i] <= k:
                    return True
        return False
    
class SlidingWindowSolution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        window = set()

        for i in range(N):
            if len(window) > k:
                window.remove(nums[i - k - 1])
            print(window)
            if nums[i] in window:
                return True
            window.add(nums[i])
        return False


if __name__ == "__main__":
    sol = SlidingWindowSolution()
    tests = [
        ([1,2,3,1,2,3], 2),
        ([1,2,3,1], 3),
        ([1,0,1,1], 1),
        ([1,2,3,1,2,3], 2),
    ]

    """
    
    {5, 1, 3}
    k = 3
    [1 2 3 4 5 1 3 1]
                   ^
    """
    for nums, k in tests:
        res = sol.containsNearbyDuplicate(nums, k)
        print(res)