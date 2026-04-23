# https://leetcode.com/problems/intervals-between-identical-elements/description/

from typing import List
from collections import defaultdict


class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        nums_positions = defaultdict(list)

        for i, num in enumerate(arr):
            nums_positions[num].append(i)

        ans = [0] * len(arr)
        for num, num_poses in nums_positions.items():
            n_left, n_right = 0, len(num_poses)

            if n_right == 1:
                continue

            left, right = 0, sum(num_poses)
            for ind in num_poses:
                ans[ind] = ind * (n_left - n_right) - left + right
                left += ind
                right -= ind
                n_left += 1
                n_right -= 1

        return ans