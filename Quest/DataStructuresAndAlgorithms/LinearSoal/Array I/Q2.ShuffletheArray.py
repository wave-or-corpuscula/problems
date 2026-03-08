# https://leetcode.com/problems/shuffle-the-array/?envType=problem-list-v2&envId=dsa-linear-shoal-array-i

from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr = []
        for i in range(n):
            arr.extend([nums[i], nums[i + n]])
        return arr
    

if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([1, 1, 1, 1, 2, 2, 2, 2], 4),
        ([2,5,1,3,4,7], 3),
        ([1,2,3,4,4,3,2,1], 4),
        ([1,1,2,2], 2),
    ]

    for test in tests:
        res = sol.shuffle(*test)
        print(res)

