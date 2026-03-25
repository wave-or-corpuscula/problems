# https://leetcode.com/problems/equal-sum-grid-partition-i/description/?envType=daily-question&envId=2026-03-25

from typing import List


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        """
        
        1 1 1
        1 1 1
        -----
        2 2 2
        
        """
        
        R = len(grid)
        C = len(grid[0])
        

        def even_parts(table, rows_count):

            rows_sum = [sum(row) for row in table]

            top_sum = rows_sum[0]
            bottom_sum = sum(rows_sum[1:])

            if top_sum > bottom_sum:
                return False

            for i in range(1, rows_count):
                if top_sum == bottom_sum:
                    return True
                
                top_sum += rows_sum[i]
                bottom_sum -= rows_sum[i]

                if bottom_sum < top_sum:
                    return False
            
            return False
        
        return even_parts(grid, R) or even_parts(zip(*grid), C)


if __name__ == "__main__":
    sol = Solution()
    tests = [
        [[1,1,1], [1,1,1], [2,2,2]],
        [[1,4],[2,3]],
        [[1,3],[2,4]],
    ]

    for grid in tests:
        res = sol.canPartitionGrid(grid)
        print(res)