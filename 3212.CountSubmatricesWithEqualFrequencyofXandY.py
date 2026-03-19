# https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/description/?envType=daily-question&envId=2026-03-19

from typing import List

from itertools import accumulate

class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        
        """

        ["X","Y",".","Y"],
        ["Y","X",".","X"],
        [".",".",".","."]

        """

        R = len(grid)

        def group_x_y(prev, cur):
            x, y = prev
            x += (cur == "X")
            y += (cur == "Y")
            return (x, y)
        
        def group_pairs(prev, cur):
            return (prev[0] + cur[0], prev[1] + cur[1])

        for i in range(R):
            grid[i][0] = (1 if grid[i][0] == 'X' else 0, 1 if grid[i][0] == 'Y' else 0)

        grid = [accumulate(row, group_x_y) for row in grid]
        grid = [accumulate(row, group_pairs) for row in zip(*grid)]

        return sum([p[0] and p[0] == p[1] for row in grid for p in row])
        

if __name__ == "__main__":
    sol = Solution()
    tests = [
        [["X","Y",".","Y"],
         ["Y","X",".","X"],
         [".",".",".","."]],
        [["X","Y","."],
         ["Y",".","."]],
        [["X","X"],["X","Y"]],
        [[".","."],[".","."]],
    ]

    for grid in tests:
        res = sol.numberOfSubmatrices(grid)
        print(res)