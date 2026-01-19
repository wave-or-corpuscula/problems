# https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/?envType=daily-question&envId=2026-01-19

from typing import List


class BrutforceSolution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        M = len(mat)
        N = len(mat[0])
        square_size = min(M, N)

        def fit_in_trashold(i: int, j: int, side: int):
            return sum(sum(row[j: j + side]) for row in mat[i: i + side]) <= threshold


        for side in range(square_size, 0, -1):
            for i in range(M - side + 1):
                for j in range(N - side + 1):
                    if fit_in_trashold(i, j, side):
                        return side
        return 0


class PrefixSolution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        M = len(mat)
        N = len(mat[0])
        pref = [[0] * (N + 1) for _ in range(M + 1)]

        for i in range(M):
            for j in range(N):
                pref[i+1][j+1] = (
                    mat[i][j]
                    + pref[i][j+1]
                    + pref[i+1][j]
                    - pref[i][j]
                )
        
        def square_sum(i, j, side):
            return (
                pref[i+side][j+side]
                - pref[i][j+side]
                - pref[i+side][j]
                + pref[i][j]
            )
        
        def can_fit(side):
            for i in range(M - side + 1):
                for j in range(N - side + 1):
                    if square_sum(i, j, side) <= threshold:
                        return True
            return False
        
        left, right = 1, min(M, N)
        answer = 0

        while left <= right:
            mid = (left + right) // 2
            if can_fit(mid):
                answer = mid
                left = mid + 1
            else:
                right = mid - 1 

        return answer



if __name__ == "__main__":
    sol = PrefixSolution()
    tests = [
        ([[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], 4),
        ([[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], 1),
        ([[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]], 6),
    ]

    for mat, treshold in tests:
        res = sol.maxSideLength(mat, treshold)
        print(res)
