# https://leetcode.com/problems/maximum-matrix-sum/description/?envType=daily-question&envId=2026-01-05

from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        negative_count = 0
        matrix_abs_sum = 0
        min_abs = abs(matrix[0][0])
        for i in range(len(matrix)):
            min_abs = min(min_abs, min(list(map(abs, matrix[i]))))
            matrix_abs_sum += sum(list(map(abs, matrix[i])))
            negative_count += len(list(filter(lambda x: x < 0, matrix[i])))
        if negative_count % 2 == 0:
            return matrix_abs_sum
        return matrix_abs_sum + -min_abs * 2
    
class PythonicSolution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0
        neg_count = 0
        min_abs = abs(matrix[0][0])

        for row in matrix:
            for x in row:
                if x < 0:
                    neg_count += 1
                    x = -x
                total += x
                if x < min_abs:
                    min_abs = x
                # min_abs = min(min_abs, x) # TODO: Сравнить скорость x = min(x, y) и if (y < x) x = y
        if neg_count % 2 == 0:
            return total
        return total - 2 * min_abs        
    

if __name__ == "__main__":
    sol = Solution()
    tests = [
        [[1,-1],[-1,1]],
        [[1,2,3],[-1,-2,-3],[1,2,3]],
        [[-1,0,-1],[-2,1,3],[3,2,2]],
        [[2,9,3],[5,4,-4],[1,7,1]],
        [[-10000,-10000,-10000],[-10000,-10000,-10000],[-10000,-10000,-10000]],
        [[-1,0,-1],[-2,1,3],[3,2,2]],
    ]

    for test in tests:
        print(sol.maxMatrixSum(test))
