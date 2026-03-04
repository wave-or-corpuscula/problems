# https://leetcode.com/problems/special-positions-in-a-binary-matrix/description/?envType=daily-question&envId=2026-03-04

from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:

        """

        2 0 1

        1 0 0   1
        0 0 1   1
        1 0 0   1
        --------
        1 1 1

        1 0 0  1
        0 1 0  1
        0 0 1  1

        """

        special_pos = 0

        spec_rows = {}
        for j, row in enumerate(mat):
            if row.count(1) == 1:
                spec_rows[row.index(1)] = j
        
        transposed = zip(*mat)
        transposed = [list(row) for row in transposed]

        for j, col in enumerate(transposed):
            if col.count(1) == 1:
                if j in spec_rows:
                    special_pos += 1

        return special_pos


if __name__ == "__main__":
    sol = Solution()
    tests = [
        [[1,0,0],
         [0,0,1],
         [1,0,0]],
        [[1,0,0],[0,1,0],[0,0,1]],
    ]

    for mat in tests:
        res = sol.numSpecial(mat)
        print(res)