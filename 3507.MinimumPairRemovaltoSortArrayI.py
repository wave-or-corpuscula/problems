# https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/description/?envType=daily-question&envId=2026-01-22

from typing import List


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def min_pair_sum(nums: List[int]) -> tuple[List[int], bool]:
            non_decr = True
            min_pair = 10**7
            first = -1
            for i in range(len(nums) - 1):
                pair_sum = nums[i] + nums[i + 1]
                if pair_sum < min_pair:
                    min_pair = pair_sum
                    first = i
                if non_decr and nums[i] > nums[i + 1]:
                    non_decr = False
            if not non_decr:
                nums[first] = nums[first] + nums[first + 1]
                nums.pop(first + 1)

            return nums, non_decr

        op_num = 0
        while True:
            nums, non_decr = min_pair_sum(nums)
            if non_decr:
                break
            op_num += 1
        return op_num
        




if __name__ == "__main__":
    sol = Solution()
    tests = [
        [5,2,3,1],
        [1,2,2],
    ]

    for nums in tests:
        res = sol.minimumPairRemoval(nums)
        print(res)