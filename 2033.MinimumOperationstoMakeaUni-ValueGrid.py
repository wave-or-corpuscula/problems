# https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/description/?envType=daily-question&envId=2026-04-28

from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        vec = [x for row in grid for x in row]
        vec.sort()
        median = vec[len(vec) // 2]

        op_cnt = 0
        for el in vec:
            diff = abs(median - el)
            if diff % x != 0:
                return -1
            op_cnt += diff // x
        
        return op_cnt




if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([[931,128],[639,712]], 73),
        ([[146]], 86),
        ([[2,4],[6,8]], 2),
        ([[1,5],[2,3]], 1),
        ([[1,2],[3,4]], 2),
    ]
    for grid, x in tests:
        res = sol.minOperations(grid, x)
        print(res)