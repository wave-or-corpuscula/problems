# https://leetcode.com/problems/construct-product-matrix/description/?envType=daily-question&envId=2026-03-24

from typing import List


class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        """
        1 2     24 12
        3 4      8  6
        
        24 12    1  1
         4  1    2  6

        """

        MOD = 12345

        R = len(grid)
        C = len(grid[0])

        suffix = [1] * (R * C)
        prefix = [1] * (R * C)

        flatten = [el for row in grid for el in row]

        for i in range(1, R * C):
            suffix[-(i + 1)] = (suffix[-i] * flatten[-i]) % MOD
            prefix[i] = (prefix[i - 1] * flatten[i - 1]) % MOD

        for i in range(R):
            for j in range(C):
                grid[i][j] = (suffix[i * C + j] * prefix[i * C + j]) % MOD

        return grid



if __name__ == "__main__":
    sol = Solution()
    tests = [
        [[12345],[2],[1]],
        [[1,2],[3,4]],
    ]

    for grid in tests:
        res = sol.constructProductMatrix(grid)
        print(res)