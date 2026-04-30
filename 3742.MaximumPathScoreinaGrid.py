# https://leetcode.com/problems/maximum-path-score-in-a-grid/description/?envType=daily-question&envId=2026-04-30

from typing import List
from math import inf

class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        def get(cell):
            if cell == 0:
                return 0, 0
            if cell == 1:
                return 1, 1
            return 1, 2  # cell == 2

        dp = [[[-inf] * (k + 1) for _ in range(n)] for _ in range(m)]

        c0, s0 = get(grid[0][0])
        if c0 <= k:
            dp[0][0][c0] = s0

        for i in range(m):
            for j in range(n):
                add_c, add_s = get(grid[i][j])

                for c in range(k + 1):
                    if dp[i][j][c] == -inf:
                        continue

                    # вниз
                    if i + 1 < m:
                        nc = c + get(grid[i+1][j])[0]
                        if nc <= k:
                            dp[i+1][j][nc] = max(
                                dp[i+1][j][nc],
                                dp[i][j][c] + get(grid[i+1][j])[1]
                            )

                    # вправо
                    if j + 1 < n:
                        nc = c + get(grid[i][j+1])[0]
                        if nc <= k:
                            dp[i][j+1][nc] = max(
                                dp[i][j+1][nc],
                                dp[i][j][c] + get(grid[i][j+1])[1]
                            )

        res = max(dp[m-1][n-1])
        return -1 if res == -inf else res


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([[0, 1],[2, 0]], 1),
        ([[0, 1],[1, 2]], 1),
    ]

    for g, k in tests:
        res = sol.maxPathScore(g, k)
        print(res)