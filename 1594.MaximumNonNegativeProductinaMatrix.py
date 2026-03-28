# https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/description/?envType=daily-question&envId=2026-03-23

from collections import deque
from typing import List

MOD = 10 ** 9 + 7

class BFSSolution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        """
        
        [-1,-2,-3]
        [-2,-3,-3]
        [-3,-3,-2]
        
        """
        def right_bottom_neighbours(i, j):
            res = []
            if i + 1 < R:
                res.append((i + 1, j))
            if j + 1 < C:
                res.append((i, j + 1))
            return res
        R = len(grid)
        C = len(grid[0])

        
        best_max = [[-float("inf")] * C for _ in range(R)]
        best_min = [[float("inf")] * C for _ in range(R)]
        queue = deque([(0, 0)])
        best_max[0][0] = grid[0][0]
        best_min[0][0] = grid[0][0]

        while queue:
            i, j = queue.popleft()

            for x, y in right_bottom_neighbours(i, j):
                val = grid[x][y]

                if val < 0:
                    new_max = val * best_min[i][j]
                    new_min = val * best_max[i][j]
                else:
                    new_max = val * best_max[i][j]
                    new_min = val * best_min[i][j]

                if new_max > best_max[x][y] or new_min < best_min[x][y]:
                    best_max[x][y] = max(best_max[x][y], new_max)
                    best_min[x][y] = min(best_min[x][y], new_min)
                    queue.append((x, y))

        return -1 if best_max[R - 1][C - 1] < 0 else best_max[R - 1][C - 1] % MOD


class DPSolution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        
        R = len(grid)
        C = len(grid[0])

        dp_max = [[-float("inf")] * C for _ in range(R)]
        dp_min = [[float("inf")] * C for _ in range(R)]

        dp_max[0][0] = grid[0][0]
        dp_min[0][0] = grid[0][0]

        def left_top_neighbours(i, j):
            return [(x, y) for x, y in [(i-1, j), (i, j-1)] if x >= 0 and y >= 0]

        for i in range(R):
            for j in range(C):
                val = grid[i][j]
                for x, y in left_top_neighbours(i, j):
                    if val > 0:
                        dp_max[i][j] = max(dp_max[i][j], dp_max[x][y] * val) 
                        dp_min[i][j] = min(dp_min[i][j], dp_min[x][y] * val)
                    else:
                        dp_max[i][j] = max(dp_max[i][j], dp_min[x][y] * val)
                        dp_min[i][j] = min(dp_min[i][j], dp_max[x][y] * val)

        return dp_max[-1][-1] % MOD if dp_max[-1][-1] >= 0 else -1




if __name__ == "__main__":
    sol = DPSolution()
    tests = [
        [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]],
        [[1,-2,1],[1,-2,1],[3,-4,1]],
        [[1,3],[0,-4]],
    ]

    for grid in tests:
        res = sol.maxProductPath(grid)
        print(res)