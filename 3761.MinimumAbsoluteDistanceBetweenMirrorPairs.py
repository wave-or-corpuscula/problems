# https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs/description/?envType=daily-question&envId=2026-04-17

from math import inf
from collections import defaultdict
from typing import List


class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def get_mirror(num: int) -> int:
            return int(str(num)[::-1])
        
        nums_poses = defaultdict(list)
        for i, num in enumerate(nums):
            nums_poses[num].append(i)
        
        best = inf

        for i, num in enumerate(nums):
            mirror_num = get_mirror(num)
            if mirror_num in nums_poses:
                inds = nums_poses[mirror_num]
                for ind in inds:
                    dist = abs(i - ind)
                    if dist > 0 and ind > i:  
                        best = min(ind - i, best)

                        if best == 1:
                            return 1
        
        return -1 if best == inf else best
    

class BetterSolution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        seen_mirrors = {}
        best = inf
        for i, num in enumerate(nums):
            if num in seen_mirrors:
                dist = i - seen_mirrors[num]
                best = min(best, dist)
            seen_mirrors[int(str(num)[::-1])] = i
        return -1 if best == inf else best



if __name__ == "__main__":
    sol = BetterSolution()
    tests = [
        [9,6,2,7,7],
        [120,21],
        [5,9,9],
        [12,21,45,33,54],
        [21,120],
    ]

    for n in tests:
        res = sol.minMirrorPairDistance(n)
        print(res)