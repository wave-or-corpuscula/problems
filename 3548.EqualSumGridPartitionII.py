# https://leetcode.com/problems/equal-sum-grid-partition-ii/description/?envType=daily-question&envId=2026-03-26

from typing import List
from collections import Counter


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        def part_grid(table: List[List[int]]) -> bool:
            R = len(table)
            C = len(table[0])
            
            rows_sum = [sum(row) for row in table]
            total = sum(rows_sum)

            top_sum = 0
            top_cells = Counter()

            bottom_sum = total
            bottom_cells = Counter()
            for row in table:
                bottom_cells.update(row)

            for i in range(0, R - 1):
                for val in table[i]:
                    top_cells[val] += 1
                    bottom_cells[val] -= 1
                    if bottom_cells[val] == 0:
                        del bottom_cells[val]

                top_sum += rows_sum[i]
                bottom_sum -= rows_sum[i]
                
                diff = top_sum - bottom_sum
                
                if diff == 0:
                    return True
                
                if diff > 0:
                    if diff in top_cells:
                        top_R = len(table[:i]) + 1
                        
                        if C > 1 and top_R > 1:
                            return True

                        if C == 1 :
                            if diff in [table[0][0], table[0][-1]]:
                                return True
                        
                        if top_R == 1 and diff in [table[0][0], table[0][-1]]:
                            return True
                else:
                    if -diff in bottom_cells:
                        cur = table[i + 1:]
                        bott_R = len(cur)
                        if C > 1 and bott_R > 1:
                            return True
                        
                        if C == 1:
                            if -diff in [cur[0][0], cur[-1][0]]:
                                return True

                        if bott_R == 1 and -diff in [table[-1][0], table[-1][-1]]:
                            return True
                        
            return False
                
        return part_grid(grid) or part_grid([list(row) for row in zip(*grid)])


if __name__ == "__main__":
    sol = Solution()
    tests = [
        # [[1],[1],[1],[1],[1],[4]],
        # [[1,8],[2,9],[3,10],[4,11],[5,12],[6,13],[7,14]],
        # [[1],[2],[3],[4],[5],[6],[7]],
        # [[100000],[86218],[100000]],
        [[100000,100000,50069,100000,100000]],
        # [[100000,90234,100000,100000,100000]],
        # [[5,5,6,2,2,2]],
        # [[1,4],[2,3]],
        # [[1,2],[3,4]],
        # [[1,2,4],[2,3,5]],
        # [[4,1,8],[3,2,6]],
    ]

    for grid in tests:
        res = sol.canPartitionGrid(grid)
        print(res)