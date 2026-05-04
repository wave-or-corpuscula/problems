# https://leetcode.com/problems/rotate-image/description/?envType=daily-question&envId=2026-05-04

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        [1,2,3]  [7,4,1]
        [4,5,6]  [8,5,2]
        [7,8,9]  [9,6,3]

        
        """
        N = len(matrix)
        for i in range(N):
            for j in range(i, N):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(N):
            matrix[i].reverse()


if __name__ == "__main__":
    sol = Solution()
    tests = [
        [[1,2,3],
         [4,5,6],
         [7,8,9]],
        [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]],
    ]
    for matrix in tests:
        sol.rotate(matrix)
        print(matrix)