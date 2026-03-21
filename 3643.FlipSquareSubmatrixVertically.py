# https://leetcode.com/problems/flip-square-submatrix-vertically/description/?envType=daily-question&envId=2026-03-21

from typing import List


class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        
        """
        [1,2,3,4]
        [5,6,7,8]
        [9,10,11,12]
        [13,14,15,16]]
        
        """
        
        for i in range(k // 2):
            for j in range(k):
                grid[x + i][y + j], grid[x + k - i - 1][y + j] = grid[x + k - i - 1][y + j], grid[x + i][y + j] 
        return grid


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12],
          [13,14,15,16]], 1, 0, 3),
        ([[3,4,2,3],
          [2,3,4,2]], 0, 2, 2)
    ]

    for grid, x, y, k in tests:
        res = sol.reverseSubmatrix(grid, x, y, k)
        print(res)