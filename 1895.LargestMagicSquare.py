# https://leetcode.com/problems/largest-magic-square/?envType=daily-question&envId=2026-01-18

from typing import List


class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def is_magic_square(x: int, y: int, size: int) -> bool:
            magic_const = sum(grid[x][y:y + size])

            for i in range(size):
                if sum(grid[x + i][y:y + size]) != magic_const:
                    return False

            for j in range(size):
                if sum(grid[x + i][y + j] for i in range(size)) != magic_const:
                    return False

            if sum(grid[x + i][y + i] for i in range(size)) != magic_const:
                return False

            if sum(grid[x + i][y + size - 1 - i] for i in range(size)) != magic_const:
                return False

            return True

        for size in range(min(m, n), 0, -1):
            for i in range(m - size + 1):
                for j in range(n - size + 1):
                    if is_magic_square(i, j, size):
                        return size
        return 1

# TODO: Переделать самому

if __name__ == "__main__":
    sol = Solution()
    tests = [
        [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]],
        [[5,1,3,1],[9,3,3,1],[1,3,3,8]]
    ]

    for test in tests:
        res = sol.largestMagicSquare(test)
        print(res)