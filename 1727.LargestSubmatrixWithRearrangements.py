# https://leetcode.com/problems/largest-submatrix-with-rearrangements/description/?envType=daily-question&envId=2026-03-17

from typing import List


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        R = len(matrix)
        C = len(matrix[0])
        heights = [0] * C
        max_area = 0

        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0

            sorted_heights = sorted(heights, reverse=True)
            max_area = max(max_area, max(h * (k + 1) for k, h in enumerate(sorted_heights)))

        return max_area


if __name__ == "__main__":
    sol = Solution()
    tests = [
        [[0,0,1],[1,1,1],[1,0,1]],
        [[1,0,1,0,1]],
        [[1,1,0],[1,0,1]],
    ]

    for m in tests:
        res = sol.largestSubmatrix(m)
        print(res)