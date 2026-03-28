# https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/description/?envType=daily-question&envId=2026-03-27

from typing import List
from collections import deque


class DequeSolution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        for i in range(len(mat)):
            original = mat[i]
            rotated = deque(mat[i])
            if i % 2 == 0:
                rotated.rotate(k)
            else:
                rotated.rotate(-k)
            if original != list(rotated):
                return False
        return True


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        R = len(mat)
        C = len(mat[0])
        k %= C

        if k == 0:
            return True
        
        def rotate_row(row, i):
            return row[-1 ** i * k:] + row[:-1 ** i * k]

        for i in range(R):
            row = rotate_row(mat[i], i)
            if mat[i] != row:
                return False
        
        return True


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([[1,2]], 1),
        ([[1,2,3],[4,5,6],[7,8,9]],       4),
        ([[1,2,1,2],[5,5,5,5],[6,3,6,3]], 2),
        ([[2,2],[2,2]],                   3),
    ]

    for mat, k in tests:
        res = sol.areSimilar(mat, k)
        print(res)