# https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/description/?envType=daily-question&envId=2026-03-18

from typing import List
from itertools import accumulate


class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        """
        7,6,3,3,4,5  18
        6,6,1,3,4,5
        6,6,1,3,4,5
        6,6,1,3,4,5

        """

        R = len(grid)
        C = len(grid[0])

        lengths = [0] * C
        bound_col = C
        count = 0

        for i in range(R):
            cur_sum = 0
            for j in range(bound_col):
                lengths[j] += grid[i][j]
                cur_sum += lengths[j]
                if cur_sum > k:
                    bound_col = j
                    break
                count += 1
            if bound_col == 0:
                break
                
        return count


class ElegantSolution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        grid = map(accumulate, grid)
        grid = map(accumulate, zip(*grid))
        return sum(val <= k for row in grid for val in row )


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([[7,6,3],[6,6,1]], 18),
        ([[7,2,9],[1,5,0],[2,6,6]], 20),
    ]

    for grid, k in tests:
        res = sol.countSubmatrices(grid, k)
        print(res)