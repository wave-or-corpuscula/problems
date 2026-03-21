# https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix/description/?envType=daily-question&envId=2026-03-20

from typing import List

inf = 10 ** 6

class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        R = len(grid)
        C = len(grid[0])

        ans = [[0 for _ in range(C - k + 1)] for _ in range(R - k + 1)]

        if k == 1:
            return ans

        def min_abs(i, j):
            best = inf

            flatten = []
            for x in range(i, i + k):
                flatten.extend(grid[x][j: j + k])
            flatten = sorted(list(set(flatten)))

            if len(flatten) == 1:
                return 0

            for i in range(1, len(flatten)):
                best = min(best, abs(flatten[i] - flatten[i - 1]))

            return best


        for i in range(R - k + 1):
            for j in range(C - k + 1):
                ans[i][j] = min_abs(i, j)

        return ans


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([[1,8],[3,-2]],     2),
        ([[3,-1]],           1),
        ([[1,-2,3],[2,3,5]], 2),
    ]

    for g, k in tests:
        res = sol.minAbsDiff(g, k)
        print(res)