# https://leetcode.com/problems/sum-of-distances/description/?envType=daily-question&envId=2026-04-23

from typing import List
from collections import defaultdict


class BrutForceSolution:
    def distance(self, nums: List[int]) -> List[int]:
        num_positions = defaultdict(list)

        for i, num in enumerate(nums):
            num_positions[num].append(i)

        result = []
        for i, num in enumerate(nums):
            positions = num_positions[num]
            equal_poses_sum = sum(abs(i - j) for j in positions if j != i)
            result.append(equal_poses_sum)
        
        return result


class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        nums_positions = defaultdict(list)

        for i, num in enumerate(nums):
            nums_positions[num].append(i)

        ans = [0] * len(nums)
        for num, num_poses in nums_positions.items():
            n_left = 0
            n_right = len(num_poses)

            if n_right == 1:
                continue

            left = 0
            right = sum(num_poses)
            for ind in num_poses:
                ans[ind] = ind * (n_left - n_right) - left + right
                left += ind
                right -= ind
                n_left += 1
                n_right -= 1

        return ans
            

if __name__ == "__main__":
    sol = Solution()
    tests = [
        [0,5,3,1,2,8,6,6,6],
        # [1,3,1,1,2],
        # [0,5,3]
    ]

    for nums in tests:
        res = sol.distance(nums)
        print(res)